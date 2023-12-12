# server.py
import grpc
from concurrent import futures
import argparse
import logging

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(parent_dir, 'grpc'))

# Import your generated server stubs
import Reddit_pb2 as reddit_pb2
import Reddit_pb2_grpc as reddit_pb2_grpc

from google.protobuf import timestamp_pb2
import time

class RedditServer(reddit_pb2_grpc.RedditServiceServicer):
    def __init__(self):
        self.posts = {}  # In-memory storage for posts
        self.comments = {}  # In-memory storage for comments

    def CreatePost(self, request, context):
        post_id = str(len(self.posts) + 1)  # Generate a post ID
        new_post = reddit_pb2.Post__pb2.Post(title=request.title, text=request.text, score=0, state=reddit_pb2.Post__pb2.PostState.PNORMAL)
        current_time = time.time()
        new_post.publication_date.FromSeconds(int(current_time))
        self.posts[post_id] = new_post
        logging.info(f'Created post with ID: {post_id}')
        return new_post

    def VotePost(self, request, context):
        post = self.posts.get(request.post_id)
        if not post:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")
        post.score += 1 if request.upvote else -1
        return post

    def GetPost(self, request, context):
        post = self.posts.get(request.post_id)
        if not post:
            context.abort(grpc.StatusCode.NOT_FOUND, "Post not found")
        return post

    def CreateComment(self, request, context):
        comment_id = str(len(self.comments) + 1)  # Generate a comment ID
        new_comment = reddit_pb2.Comment__pb2.Comment(comment_id=comment_id, post_id=request.post_id, parent_comment_id=request.parent_comment_id, 
                                                    text=request.text, author=request.author, score=0, state=reddit_pb2.Comment__pb2.CommentState.CNORMAL, has_replies=False)
        self.comments[comment_id] = new_comment
        current_time = time.time()
        new_comment.publication_date.FromSeconds(int(current_time))
        logging.info(f'Created comment with ID: {comment_id}')
        return new_comment

    def VoteComment(self, request, context):
        comment = self.comments.get(request.comment_id)
        if not comment:
            context.abort(grpc.StatusCode.NOT_FOUND, "Comment not found")
        comment.score += 1 if request.upvote else -1
        return comment
    
    def GetTopComments(self, request, context):
        # Filter comments by post_id and sort them by score in descending order
        filtered_comments = [comment for comment_id, comment in self.comments.items() if comment.post_id == request.post_id]
        sorted_comments = sorted(filtered_comments, key=lambda c: c.score, reverse=True)

        # Get top N comments
        top_comments = sorted_comments[:request.n]

        # Prepare the response
        response = reddit_pb2.TopCommentsResponse()
        for comment in top_comments:
            # Check if the comment has replies
            has_replies = any(child_comment.parent_comment_id == comment.comment_id for child_comment in self.comments.values())
            response.comments.add(
                comment_id=comment.comment_id,
                author=comment.author,
                score=comment.score,
                state=comment.state,
                publication_date=comment.publication_date,
                text=comment.text,
                post_id=comment.post_id,
                parent_comment_id=comment.parent_comment_id,
                has_replies=has_replies
            )

        return response

     # Function to get top N replies for a given comment
    def get_top_replies(self, comment_id, n):
            replies = [c for c in self.comments.values() if c.parent_comment_id == comment_id]
            sorted_replies = sorted(replies, key=lambda c: c.score, reverse=True)
            return sorted_replies[:n]

    def ExpandCommentBranch(self, request, context):
        # First, get top N comments that are direct replies to the given comment
        top_comments = self.get_top_replies(request.comment_id, request.n)

        # Prepare the response
        response = reddit_pb2.CommentBranchResponse()

        # For each of these top comments, find their top N replies and add to the response
        for comment in top_comments:
            comment_with_replies = response.comments.add(comment=comment)
            top_replies = self.get_top_replies(comment.comment_id, request.n)
            comment_with_replies.replies.extend(top_replies)

        return response

def serve(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    reddit_pb2_grpc.add_RedditServiceServicer_to_server(RedditServer(), server)
    server.add_insecure_port(f'{host}:{port}')
    server.start()
    server.wait_for_termination()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Reddit gRPC server')
    parser.add_argument('--host', default='localhost', help='Host to run gRPC server on')
    parser.add_argument('--port', type=int, default=50051, help='Port to run gRPC server on')
    args = parser.parse_args()

    serve(args.host, args.port)

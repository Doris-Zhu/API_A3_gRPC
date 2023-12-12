# client.py
import grpc

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(parent_dir, 'grpc'))

# Import your generated server stubs
import Reddit_pb2 as reddit_pb2
import Reddit_pb2_grpc as reddit_pb2_grpc

class RedditClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = reddit_pb2_grpc.RedditServiceStub(self.channel)

    def create_post(self, title, text):
        request = reddit_pb2.CreatePostRequest(title=title, text=text)
        return self.stub.CreatePost(request)
    
    def vote_post(self, post_id, upvote):
        request = reddit_pb2.VotePostRequest(post_id=post_id, upvote=upvote)
        return self.stub.VotePost(request)
    
    def get_post(self, post_id):
        request = reddit_pb2.GetPostRequest(post_id=post_id)
        return self.stub.GetPost(request)
    
    def create_comment(self, post_id, parent_comment_id, text, author):
        request = reddit_pb2.CreateCommentRequest(post_id=post_id, parent_comment_id=parent_comment_id, text=text, author=author)
        return self.stub.CreateComment(request)
    
    def vote_comment(self, comment_id, upvote):
        request = reddit_pb2.VoteCommentRequest(comment_id=comment_id, upvote=upvote)
        return self.stub.VoteComment(request)
    
    def get_top_comment(self, post_id, n):
        request = reddit_pb2.GetTopCommentsRequest(post_id=post_id, n=n)
        return self.stub.GetTopComments(request)
    
    def expand_comment_branch(self, comment_id, n):
        request = reddit_pb2.ExpandCommentBranchRequest(comment_id=comment_id, n=n)
        return self.stub.ExpandCommentBranch(request)

def retrieve_and_expand_post(client, post_id, num_comments=1, num_replies=1):
    """
    Retrieves a post, its top comments, and expands the most upvoted comment.

    :param client: Instance of the API client.
    :param post_id: ID of the post to retrieve.
    :param num_comments: Number of top comments to retrieve.
    :param num_replies: Number of replies to retrieve for the top comment.
    :return: Tuple of (Post, most upvoted Comment, most upvoted Reply or None)
    """

    # Retrieve the post
    post = client.get_post(post_id)

    # Get the top comments for the post
    top_comments_response = client.get_top_comments(post_id, num_comments)
    if not top_comments_response.comments:
        return post, None, None  # No comments found

    # Assuming comments are sorted by score in descending order
    top_comment = top_comments_response.comments[0]

    # Expand the most upvoted comment to get its replies
    comment_replies_response = client.expand_comment_branch(top_comment.comment_id, num_replies)
    if not comment_replies_response.comments:
        return post, top_comment, None  # No replies found

    # Get the most upvoted reply
    top_reply = comment_replies_response

    return post, top_comment, top_reply


if __name__ == '__main__':
    client = RedditClient('localhost', 50051)
    response1 = client.create_post("Sample Title", "This is a sample post text.")
    print(f"Post Created: {response1.title}, {response1.text},  {response1.score}")
    response2 = client.vote_post("1", True)
    print(f"Post: {response2.title}, {response2.score}")
    response3 = client.get_post("1")
    print(f"Post: {response3.title}, {response3.text}, {response3.score}")
    response4 = client.create_comment("1", "0", "comment text", "author a")
    print(f"Comment created: {response4.text}, {response4.author}")
    response5 = client.vote_comment("1", False)
    print(f"Comment: {response5.score}")
    response6 = client.get_top_comment("1", 2)
    print(response6)
    response7 = client.expand_comment_branch("2", 1)
    print(response7)
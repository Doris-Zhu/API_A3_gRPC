import unittest
from unittest.mock import Mock

import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(parent_dir, 'main', 'reddit', 'client'))
from reddit_client import retrieve_and_expand_post

sys.path.insert(0, os.path.join(parent_dir, 'main', 'reddit', 'grpc'))
import Reddit_pb2 as reddit_pb2


class TestReddit(unittest.TestCase):
    def setUp(self):
        # Mock the API client
        self.mock_client = Mock()

        def get_post_side_effect(post_id):
            if post_id == "1":
                return reddit_pb2.Post__pb2.Post(title="Title 1", text='Text 1', score=10, state=reddit_pb2.Post__pb2.PostState.PNORMAL)
            elif post_id == "2":
                return reddit_pb2.Post__pb2.Post(title="Title 2", text='Text 2', score=20, state=reddit_pb2.Post__pb2.PostState.PNORMAL)
            else:
                return None  # or some default value

        self.mock_client.get_post.side_effect = get_post_side_effect

        def make_mock_comment(comment_id):
            # return reddit_pb2.Comment__pb2.Comment(
            #     comment_id=comment_id,
            #     post_id=post_id,
            #     parent_comment_id="",  # Assuming it's a top-level comment
            #     text=f"Comment text for {comment_id}",
            #     author=f"Author {comment_id}",
            #     score=score,
            #     state=reddit_pb2.Comment__pb2.CommentState.CNORMAL,
            #     # For publication_date, you need to create a Timestamp object or set it appropriately
            #     has_replies=False
            # )
            if comment_id == '1':
                return reddit_pb2.Comment__pb2.Comment(
                comment_id='1',
                post_id='1',
                parent_comment_id="",  # Assuming it's a top-level comment
                text=f"Comment text for {comment_id}",
                author=f"Author {comment_id}",
                score=2,
                state=reddit_pb2.Comment__pb2.CommentState.CNORMAL,
                # For publication_date, you need to create a Timestamp object or set it appropriately
                has_replies=True
            )
            if comment_id == '2':
                return reddit_pb2.Comment__pb2.Comment(
                comment_id='2',
                post_id='1',
                parent_comment_id="",  # Assuming it's a top-level comment
                text=f"Comment text for {comment_id}",
                author=f"Author {comment_id}",
                score=5,
                state=reddit_pb2.Comment__pb2.CommentState.CNORMAL,
                # For publication_date, you need to create a Timestamp object or set it appropriately
                has_replies=False
            )
            if comment_id == '3':
                return reddit_pb2.Comment__pb2.Comment(
                comment_id='3',
                post_id='1',
                parent_comment_id='1',  # Assuming it's a top-level comment
                text=f"Comment text for {comment_id}",
                author=f"Author {comment_id}",
                score=3,
                state=reddit_pb2.Comment__pb2.CommentState.CNORMAL,
                # For publication_date, you need to create a Timestamp object or set it appropriately
                has_replies=False
            )
            if comment_id == '4':
                return reddit_pb2.Comment__pb2.Comment(
                comment_id='4',
                post_id='1',
                parent_comment_id='3',  # Assuming it's a top-level comment
                text=f"Comment text for {comment_id}",
                author=f"Author {comment_id}",
                score=3,
                state=reddit_pb2.Comment__pb2.CommentState.CNORMAL,
                # For publication_date, you need to create a Timestamp object or set it appropriately
                has_replies=False
            )

        def generate_mock_top_comments_response(post_id, num_comments):
            response = reddit_pb2.TopCommentsResponse()
            for i in range(num_comments):
                mock_comment = make_mock_comment(str(i + 1))
                response.comments.add().MergeFrom(mock_comment)
            return response

        self.mock_client.get_top_comments.side_effect = generate_mock_top_comments_response

        def generate_mock_comment_branch_response(comment_id, num_replies, depth=2):
            # Create a response object
            response = reddit_pb2.CommentBranchResponse()

            # Generate mock replies (top-level comments)
            for i in range(num_replies):
                # Create the top-level comment
                top_level_comment_id = f"{i + 3}"
                top_level_comment = make_mock_comment(top_level_comment_id)
                response.comments.add().MergeFrom(top_level_comment)

                for j in range(num_replies):  # Assuming the same number of replies per comment
                    sub_comment = make_mock_comment(f"{i + 3 + j + 1}")
                    response.comments.add().MergeFrom(sub_comment)

            return response

        # Assign the side effect to the mock client's get_top_replies method
        self.mock_client.expand_comment_branch.side_effect = generate_mock_comment_branch_response


    def test_retrieve_and_expand_post(self):
        # Test when API is accessible
        post, top_comment, branch = retrieve_and_expand_post(self.mock_client, "2")
        self.assertIsNotNone(post)
        print(post, top_comment, branch)
       
if __name__ == '__main__':
    unittest.main()

# client.py
import grpc

# Import your generated client stubs
import reddit_pb2
import reddit_pb2_grpc

class RedditClient:
    def __init__(self, host, port):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = reddit_pb2_grpc.RedditServiceStub(self.channel)

    def create_post(self, title, text):
        request = reddit_pb2.CreatePostRequest(title=title, text=text)
        return self.stub.CreatePost(request)

    # Implement other client methods

if __name__ == '__main__':
    client = RedditClient('localhost', 50051)
    # Test client methods

# server.py
import grpc
from concurrent import futures
import argparse

# Import your generated server stubs
import reddit_pb2
import reddit_pb2_grpc

class RedditServer(reddit_pb2_grpc.RedditServiceServicer):
    def CreatePost(self, request, context):
        # Implement logic here
        return reddit_pb2.Post(title=request.title, text=request.text, author="dummy_author", score=0, state=reddit_pb2.NORMAL)


    # Implement other service methods

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

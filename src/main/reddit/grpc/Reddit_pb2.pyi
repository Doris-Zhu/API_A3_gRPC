import User_pb2 as _User_pb2
import Post_pb2 as _Post_pb2
import Comment_pb2 as _Comment_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreatePostRequest(_message.Message):
    __slots__ = ("title", "text", "video_url", "image_url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    video_url: str
    image_url: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

class VotePostRequest(_message.Message):
    __slots__ = ("post_id", "upvote")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    upvote: bool
    def __init__(self, post_id: _Optional[str] = ..., upvote: bool = ...) -> None: ...

class GetPostRequest(_message.Message):
    __slots__ = ("post_id",)
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    def __init__(self, post_id: _Optional[str] = ...) -> None: ...

class CreateCommentRequest(_message.Message):
    __slots__ = ("comment_id", "post_id", "parent_comment_id", "text", "author")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    post_id: str
    parent_comment_id: str
    text: str
    author: str
    def __init__(self, comment_id: _Optional[str] = ..., post_id: _Optional[str] = ..., parent_comment_id: _Optional[str] = ..., text: _Optional[str] = ..., author: _Optional[str] = ...) -> None: ...

class VoteCommentRequest(_message.Message):
    __slots__ = ("comment_id", "upvote")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    UPVOTE_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    upvote: bool
    def __init__(self, comment_id: _Optional[str] = ..., upvote: bool = ...) -> None: ...

class GetTopCommentsRequest(_message.Message):
    __slots__ = ("post_id", "n")
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    post_id: str
    n: int
    def __init__(self, post_id: _Optional[str] = ..., n: _Optional[int] = ...) -> None: ...

class TopCommentsResponse(_message.Message):
    __slots__ = ("comments",)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_Comment_pb2.Comment]
    def __init__(self, comments: _Optional[_Iterable[_Union[_Comment_pb2.Comment, _Mapping]]] = ...) -> None: ...

class ExpandCommentBranchRequest(_message.Message):
    __slots__ = ("comment_id", "n")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    n: int
    def __init__(self, comment_id: _Optional[str] = ..., n: _Optional[int] = ...) -> None: ...

class CommentBranchResponse(_message.Message):
    __slots__ = ("comments",)
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    comments: _containers.RepeatedCompositeFieldContainer[_Comment_pb2.Comment]
    def __init__(self, comments: _Optional[_Iterable[_Union[_Comment_pb2.Comment, _Mapping]]] = ...) -> None: ...

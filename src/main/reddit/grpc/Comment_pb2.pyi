from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CNORMAL: _ClassVar[CommentState]
    CHIDDEN: _ClassVar[CommentState]
CNORMAL: CommentState
CHIDDEN: CommentState

class Comment(_message.Message):
    __slots__ = ("comment_id", "author", "score", "state", "publication_date", "text", "post_id", "parent_comment_id", "has_replies")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    POST_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_REPLIES_FIELD_NUMBER: _ClassVar[int]
    comment_id: str
    author: str
    score: int
    state: CommentState
    publication_date: _timestamp_pb2.Timestamp
    text: str
    post_id: str
    parent_comment_id: str
    has_replies: bool
    def __init__(self, comment_id: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[CommentState, str]] = ..., publication_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., text: _Optional[str] = ..., post_id: _Optional[str] = ..., parent_comment_id: _Optional[str] = ..., has_replies: bool = ...) -> None: ...

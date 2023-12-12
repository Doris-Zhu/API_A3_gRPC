from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PNORMAL: _ClassVar[PostState]
    PLOCKED: _ClassVar[PostState]
    PHIDDEN: _ClassVar[PostState]
PNORMAL: PostState
PLOCKED: PostState
PHIDDEN: PostState

class Post(_message.Message):
    __slots__ = ("title", "text", "author", "score", "state", "publication_date", "video_url", "image_url")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PUBLICATION_DATE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    title: str
    text: str
    author: str
    score: int
    state: PostState
    publication_date: _timestamp_pb2.Timestamp
    video_url: str
    image_url: str
    def __init__(self, title: _Optional[str] = ..., text: _Optional[str] = ..., author: _Optional[str] = ..., score: _Optional[int] = ..., state: _Optional[_Union[PostState, str]] = ..., publication_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., video_url: _Optional[str] = ..., image_url: _Optional[str] = ...) -> None: ...

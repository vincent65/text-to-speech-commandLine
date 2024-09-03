from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Text(_message.Message):
    __slots__ = ("text",)
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class Speech(_message.Message):
    __slots__ = ("Audio",)
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    Audio: bytes
    def __init__(self, Audio: _Optional[bytes] = ...) -> None: ...

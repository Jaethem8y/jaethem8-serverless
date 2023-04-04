import typing as typ
import enum
import datetime
from pydantic import BaseModel

class BlockType(str, enum.Enum):
    code:"code"
    writing:"writing"
    image:"image"

class Block(BaseModel):
    type:BlockType
    slug: typ.Union[bytes,str]
    place: int

class Content(BaseModel):
    header: typ.Optional[str]
    block: Block
    place: int

class Post(BaseModel):
    title: str
    desciption: str
    frontend: str
    backend: str
    other: str
    date: datetime.datetime
    content: Content
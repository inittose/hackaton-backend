import pydantic
import uuid
from enum import Enum

class Creds(pydantic.BaseModel):
    username: str
    password: str

class Creds2(pydantic.BaseModel):
    password1: str
class User(pydantic.BaseModel):
    id: uuid.UUID
    username: str
class Maindata(pydantic.BaseModel):
    title: str
    description: str

class Create(pydantic.BaseModel):
    title: str
    owner: str
    description: str
    acsess: bool

class Acsess1(Enum):
    Yes = "True"
    No = "False"

class Answer1(Enum):
    Yes = "Yes"
    No = "No"

class Answer(pydantic.BaseModel):
    number: int
    answer: Answer1
class Question(pydantic.BaseModel):
    number: int
    question: str
class Get(pydantic.BaseModel):
    title: str
    acsess: bool

class Q(pydantic.BaseModel):
    question: str


















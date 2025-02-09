from pydantic import BaseModel
from typing import Optional as Opt


class UserCreate(BaseModel):
    username: str

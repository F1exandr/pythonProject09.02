from pydantic import BaseModel
from typing import Optional as Opt


class UserView(BaseModel):
    id: int
    username: str


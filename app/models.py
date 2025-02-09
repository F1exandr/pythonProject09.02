from datetime import datetime
from enum import Enum
from typing import Optional, List

from pydantic import BaseModel
from sqlmodel import Field, SQLModel, Relationship



class UserHomeLink(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='user.id')
    home_id: Optional[int] = Field(default=None, primary_key=True, foreign_key='home.id')

class UserBase(SQLModel):
    pass





class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field()
    password: Optional[str] = Field()
    email: Optional[str] = Field()

    home: list["Home"]= Relationship(back_populates="user", link_model=UserHomeLink)


class HomeBase(SQLModel):
    pass

class Home(HomeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    city: Optional[str]
    user: list["User"]=Relationship(back_populates="home", link_model=UserHomeLink)
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette.responses import Response
from starlette.status import HTTP_202_ACCEPTED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_406_NOT_ACCEPTABLE, HTTP_405_METHOD_NOT_ALLOWED

from database import get_session
from models import User, Home


router = APIRouter()


@router.post("/user_add_city/{id}")
def user_add_city(id: int, session: Session = Depends(get_session)):
    user = session.get(User, id)
    home1 = session.get(Home, 1)
    home2 = session.get(Home, 2)

    user.home=[home1,home2]
    session.commit()
    session.refresh(user)

    user = session.get(User, 2)
    home1 = session.get(Home, 1)
    # home2 = session.get(Home, 2)

    user.home = [home1]
    session.commit()
    session.refresh(user)
    return user.home

@router.get("/user_city/{id}")
def user_city(id: int, session: Session = Depends(get_session)):
    user = session.get(User, id)
    return user.home
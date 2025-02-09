from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from starlette.responses import Response
from starlette.status import HTTP_202_ACCEPTED, HTTP_401_UNAUTHORIZED, HTTP_200_OK, HTTP_201_CREATED, \
    HTTP_406_NOT_ACCEPTABLE, HTTP_405_METHOD_NOT_ALLOWED

from database import get_session
from models import User

router = APIRouter()


@router.post('/register', summary='Регистрация пользователя')
async def register(data: UserCreate = Depends(), session: Session = Depends(get_session)):


    data = data.dict()
    data = User(**data)
    session.add(data)
    session.commit()
    return Response(status_code=HTTP_201_CREATED)

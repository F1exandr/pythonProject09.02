from fastapi import APIRouter


router = APIRouter()

@router.post('/tovar')
async def tovar(tovar_name: str):
    return {"tovar_name":tovar_name}

@router.get('/add_tovar')
async def add_tovar(toar_add: str):
    return {"toar_add":toar_add}

from fastapi import FastAPI, APIRouter
from base import Doctor
from services.doctor import add_doctor

router = APIRouter(
    prefix="/doctor"
)

@router.post('/')
async def add_details(params: Doctor):
    # print(params, "v")
    result = await add_doctor(params.dict())
    if result :
        return True
    else:
        return False

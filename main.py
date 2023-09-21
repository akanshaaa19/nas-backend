from connection import (
    fetch_one,
    fetch_all,
    add_otp
)
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from endpoints.doctor import router
from base import Otp

app = FastAPI()

origins = ['http://localhost:5173 ']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_credentials=["*"],
    allow_methods=["*"]
) 

app.include_router(router)


@app.get("/")
async def read_root():
    response = await fetch_one()
    return response

@app.post("/")
async def post_co(otp: Otp):
    # doc = otp
    print(otp)
    res =await add_otp(otp)
    if res: 
        return res
    return res 



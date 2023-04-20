from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
# from main_data.getToken import token
from main_data.getData import count, stateOk
import numpy as np

app_router = APIRouter()


stateFail =[0 for i in range(0,7)]
for i in range(0,7):
    stateFail[i]=count[i]-stateOk[i]


@app_router.get("/chart-data")
async def get_data():
    return {"count": count, "stateOk": stateOk, "stateFail": stateFail}

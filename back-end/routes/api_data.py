from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from main_data.getData import data

app_router = APIRouter()


@app_router.get("/data")
async def get_data():
    print(data)
    return {"data": data}

from fastapi import APIRouter, HTTPException, status
from bson import ObjectId
from main_data.getToken import token

app_router = APIRouter()


@app_router.get("/data")
async def get_data():
    return {"token": token}

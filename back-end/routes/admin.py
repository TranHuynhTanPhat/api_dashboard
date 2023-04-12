from fastapi import APIRouter, HTTPException, status

from models.user import User
from config.db import db
from schemas.user import userEntity, usersEntity
from bson import ObjectId

admin_router = APIRouter()

# LOGIN ADMIN
@admin_router.get("/admin/login")
async def admin_login(email: str, password: str):
    try:
        user = userEntity(db.find_one({"email": email, "password": password}))
        if user["role"] == 0:
            return {
                "status": "success",
                "data": {"id": user["id"], "email": user["email"]},
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid"
            )
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid")
from fastapi import APIRouter, HTTPException, status
from app.models.user import User
from app.config.db import db
from app.schemas.user import userEntity, usersEntity
from bson import ObjectId

app_router = APIRouter()


# LOGIN ADMIN
@app_router.post("/admin/login")
async def admin_login(email: str, password: str):
    try:
        user = userEntity(db.find_one({"email": email, "password": password}))
        if user["role"] == 0:
            return {
                "data": {
                    "id": result["id"],
                    "email": result["email"],
                    "status": result["status"],
                    "role": result["role"],
                },
                "token": "token",
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid"
            )
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid")

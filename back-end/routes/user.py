from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user_router = APIRouter()


# retrieve
@user_router.get('/users')
async def find_all_users():
    result = usersEntity(conn.find())

    return {"status": "ok", "data": result}


@user_router.get('/user/{id}')
async def find_user_by_id(id: str):
    result = userEntity(conn.find_one({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


# post
@user_router.post("/user/register")
async def register(user: User):
    _id = conn.insert_one(dict(user))
    result = userEntity(conn.find_one({"_id": _id.inserted_id}))
    return {"status": "ok", "data": result}


# update
@user_router.put('/user/{id}')
async def update_user(id: str, user: User):
    conn.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    result = userEntity(conn.find_one({"_id": ObjectId(id)}))
    return {"status": "ok", "data": result}


# delete
@user_router.delete("/user/{id}")
async def delete_user(id: str):
    conn.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}

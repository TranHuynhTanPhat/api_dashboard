from fastapi import APIRouter, HTTPException, status

from models.user import User
from config.db import db
from schemas.user import userEntity, usersEntity
from bson import ObjectId

user_router = APIRouter()


# RETRIEVE ALL ACCOUNT
@user_router.get("/users")
async def find_all_users():
    result = usersEntity(db.find())
    return {"status": "success", "data": result}


# RETRIEVE ACCOUNT BY ID
@user_router.get("/user/{id}")
async def find_user_by_id(id: str):
    result = userEntity(db.find_one({"_id": ObjectId(id)}))
    return {"status": "success", "data": result}


# REGISTER ACCOUNT
@user_router.post("/user/register")
async def register(user: User):
    # check existed email
    check = usersEntity(db.find({"email": str(user.email)}))

    # if email's existed return status 409 (admin's role is 1)
    # if role = 0 or out range[0;2] return status 401
    # else return status 200

    if len(check) != 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Can't create account with email: {user.email}",
        )
    elif int(user.role) == 0 or int(user.role) > 2 or int(user.role) < 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Can't create account"
        )
    elif user.email == "" or user.password == "":
        raise HTTPException(status_code=406, detail="Not Acceptable")
    else:
        _id = db.insert_one(dict(user))
        result = userEntity(db.find_one({"_id": _id.inserted_id}))
        return {
            "status": "success",
            "message": "Successfully created user: " + user.email,
            "data": {
                "id": result["id"],
                "email": result["email"],
            },
        }


# UPDATE ACCOUNT BY ID
@user_router.put("/user/{id}")
async def update_user(id: str, user: User):
    # check existed email
    check = usersEntity(db.find({"email": str(user.email)}))

    # if email's existed return status 409 (admin's role is 1)
    # if role = 0 or out range[0;2] return status 401
    # else return status 200

    if len(check) != 0:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Can't create account with email: {user.email}",
        )
    elif int(user.role) == 0 or int(user.role) > 2 or int(user.role) < 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Can't create account"
        )
    else:
        db.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
        result = userEntity(db.find_one({"_id": ObjectId(id)}))
        return {
            "status": "success",
            "data": {"id": result["id"], "email": result["email"]},
        }


# DELETE ACCOUNT BY ID
@user_router.delete("/user/{id}")
async def delete_user(id: str):
    check = userEntity(db.find_one({"_id": ObjectId(id)}))
    if check["role"] != 0:
        db.find_one_and_delete({"_id": ObjectId(id)})
        return {"status": "success"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You can delete this account!",
        )



# LOGIN USER
@user_router.get("/user/login")
async def user_login(email: str, password: str):
    try:
        return {"status": "success", "data": {email, password}}

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Login failed"
        )

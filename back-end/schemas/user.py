def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "password": item["password"],
        "status": item["status"],
        "role":item["role"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

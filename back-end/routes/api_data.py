from fastapi import APIRouter, HTTPException, status, File, UploadFile, Request
from config.db import db
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from main_data.getData import times, stateOk, inspection, data
import numpy as np
from datetime import date, datetime
import base64


app_router = APIRouter()


stateFail = [0 for i in range(0, 7)]
for i in range(0, 7):
    stateFail[i] = times[i] - stateOk[i]


@app_router.get("/chart-data")
async def chart_data():
    return {"count": times, "stateOk": stateOk, "stateFail": stateFail}


@app_router.get("/today-users")
async def today_users():
    allUsers = usersEntity(db.find())
    countUserToday = 0
    countUserThisOneLastWeek = 0
    pc = 0
    total = True
    for us in allUsers:
        arrAccessed = us["accessed_at"]
        for a in arrAccessed:
            if a.date() == date.today():
                countUserToday += 1
            elif abs(date.today() - a.date()).days == 7:
                countUserThisOneLastWeek += 1
    if countUserThisOneLastWeek == 0:
        pc = round((100 * (countUserToday / len(allUsers))), 2)
    else:
        total = False
        pc = round(
            100
            * (countUserToday - countUserThisOneLastWeek)
            / countUserThisOneLastWeek,
            2,
        )
    return {
        "todayUsers": (format(countUserToday, ",d")),
        "percent": pc,
        "total": total,
    }


@app_router.get("/new-clients")
async def new_clients():
    newClientsThisQuarter = 0
    ClientsLastQuarter = 0
    pc = 0
    quarterNow = int(datetime.now().month) // 4 + 1
    allUsers = usersEntity(db.find())

    for u in allUsers:
        quaterU = int(u["created_at"].month) // 4 + 1
        if quaterU == quarterNow:
            newClientsThisQuarter += 1
        elif quarterU == quarterNow - 1:
            ClientsLastQuarter += 1

    if ClientsLastQuarter == 0:
        pc = -1
    else:
        total = False
        pc = round(
            100 * (newClientsThisQuarter - ClientsLastQuarter) / ClientsLastQuarter, 2
        )

    return {
        "newClients": (format(newClientsThisQuarter, ",d")),
        "percent": pc,
    }


@app_router.get("/status-success")
async def status_success():
    percent = round(100 * (sum(stateOk) / sum(times)), 2)
    return {"state_ok": (format(sum(stateOk), ",d")), "percent": percent}


@app_router.get("/total-check-times")
async def status_fail():
    return {"total_check": (format(sum(times), ",d"))}


@app_router.get("/get-inspection")
async def get_inspection():
    return {"data": inspection}


@app_router.get("/get-inspection-detail")
async def get_inspection_detail(id: str):
    try:
        detail_predict = []
        angid = [0 for i in range(0, 7)]
        listA = data[id]
        for detail in listA:
            temp = listA[detail]
            num = int(temp["angle_id"])
            angid[num - 1] += 1

            time = datetime.fromisoformat(temp["date"])
            dt = time.strftime("%Y-%m-%d %H:%M:%S").split(" ")

            detail_predict.append(
                {
                    "date": dt[0],
                    "time": dt[1],
                    "angle_id": temp["angle_id"],
                    "status": temp["status"],
                    "predict_result": temp["predict_result"],
                }
            )
        return {"angle_id": angid, "all_details": detail_predict}
    except:
        raise HTTPException(status_code=500)


@app_router.post("/upload-avatar")
async def upload_avatar(file: UploadFile, id: str):
    allowedFiles = {
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/tiff",
        "image/bmp",
        "video/webm",
    }
    if file.content_type in allowedFiles:
        user = userEntity(db.find_one({"_id": ObjectId(id)}))
        try:
            contents = base64.b64encode(file.file.read())
            # with open("uploaded_" + file.filename, "wb") as f:
            #     f.write(contents)

            # print(contents)

            # user["image"] = contents
            # db.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()

        return {"message": f"Successfuly uploaded {file.filename}"}
    raise HTTPException(status_code=415, detail="Unsupported Media Type")

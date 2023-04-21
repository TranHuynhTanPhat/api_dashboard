from fastapi import APIRouter, HTTPException, status
from config.db import db
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from main_data.getData import count, stateOk
import numpy as np
from datetime import date


app_router = APIRouter()


stateFail = [0 for i in range(0, 7)]
for i in range(0, 7):
    stateFail[i] = count[i] - stateOk[i]


@app_router.get("/chart-data")
async def chart_data():
    return {"count": count, "stateOk": stateOk, "stateFail": stateFail}


@app_router.get("/today-users")
async def today_users():
    allUsers = usersEntity(db.find())
    countUserToday = 0
    countUserThisOneLastWeek = 0
    pc = 0
    for us in allUsers:
        dtime = us["created_at"].date()
        tday = date.today()
        if dtime == tday:
            countUserToday += 1
        if abs(tday - dtime).days == 7:
            countUserThisOneLastWeek += 1

    if countUserThisOneLastWeek == 0:
        pc = 100
    else:
        pc = (
            100 * (countUserToday - countUserThisOneLastWeek) / countUserThisOneLastWeek
        )
    return {"todayUsers": countUserToday, "percentThisOneWeek": pc}




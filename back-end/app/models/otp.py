from pydantic import BaseModel
from datetime import datetime


class otp(BaseModel):
    code: int
    time: datetime
    userId: str

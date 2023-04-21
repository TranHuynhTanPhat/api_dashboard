from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    email:str =''
    password: str  =''
    status: int = 0
    role: int = 1
    created_at: datetime = datetime.now()
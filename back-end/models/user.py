from pydantic import BaseModel

class User(BaseModel):
    email:str
    password: str 
    status: int
    role: int
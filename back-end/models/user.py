from pydantic import BaseModel

class User(BaseModel):
    email:str =''
    password: str  =''
    status: int = 0
    role: int = 0
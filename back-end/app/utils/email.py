from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from starlette.requests import Request
from starlette.responses import JSONResponse
from pydantic import EmailStr, BaseModel
from typing import List

app = FastAPI()

class EmailSchema(BaseModel):
   email: List[EmailStr]

conf = ConnectionConfig(
   MAIL_USERNAME=from_,
   MAIL_PASSWORD="************",
   MAIL_PORT=587,
   MAIL_SERVER="smtp.gmail.com",
   MAIL_TLS=True,
   MAIL_SSL=False
)

message = MessageSchema(
       subject="Verify API-Dashboard",
       recipients=email.dict().get("email"),  # List of recipients, as many as you can pass  
       body=template,
       subtype="html"
       )
fm = FastMail(conf)
await fm.send_message(message)
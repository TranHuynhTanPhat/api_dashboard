from pymongo import MongoClient


client = MongoClient("mongodb+srv://dbAPIDashboard:dbAPIDashboard@cluster0.5iliejt.mongodb.net/?retryWrites=true&w=majority")
db = client.api_dashboard_application
conn=db["api_dashboard"]



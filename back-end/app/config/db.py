from pymongo import MongoClient


client = MongoClient("mongodb+srv://dbAPIDashboard:dbAPIDashboard@cluster0.5iliejt.mongodb.net/?retryWrites=true&w=majority")
conn = client.api_dashboard_application
db=conn["api_dashboard"]



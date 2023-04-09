from pymongo import MongoClient


client = MongoClient("mongodb+srv://dbAPIDashboard:dbAPIDashboard@mern-learnit.qg9qu6w.mongodb.net/?retryWrites=true&w=majority")
db = client.api_dashboard_application


conn=db["api_dashboard"]
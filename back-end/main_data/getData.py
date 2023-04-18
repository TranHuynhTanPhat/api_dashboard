import requests
import json
from main_data.getToken import token
from models.routerModel import routerModel

url = "http://cads-api.fpt.vn/fiber-detection/v2/using_json_inf/2022/12"

payload = "angle_id"
headers = {
  'Content-Type': 'application/json',
  'Authorization': token
}

response = requests.request("POST", url, headers=headers)
data=json.loads(response.text)


listData=[]
for lv1 in data:
  ob1=[]
  for lv2 in data[lv1]:
    temp = data[lv1][lv2]
    m = routerModel(lv2,temp['date'],temp['angle_id'],temp['status'], temp['predict_result'])
    ob1.append(m)
  listData.append(ob1)



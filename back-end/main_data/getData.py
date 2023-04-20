import requests
import json
from main_data.getToken import token
from datetime import datetime
from array import array

url = "http://cads-api.fpt.vn/fiber-detection/v2/using_json_inf/2022/12"

payload = "angle_id"
headers = {
    'Content-Type': 'application/json',
    'Authorization': token
}



response = requests.request("POST", url, headers=headers)
data = json.loads(response.text)


count = [0 for i in range(0, 7)]
stateOk = [0 for i in range(0, 7)]


for lv1 in data:
    for lv2 in data[lv1]:
        temp = data[lv1][lv2]
        num = int(temp['angle_id'])
        status = temp['status']
        count[num-1] += 1
        if status == 'ok':
            stateOk[num-1] += 1
        



# for lv1 in data:
#     for lv2 in data[lv1]:
#         temp = data[lv1][lv2]
#         value = temp['date']
#         date = datetime.fromisoformat(value).date()
#         f.write(str(date) + "\n")


# listData=[]
# for lv1 in data:
#   ob1=[]
#   for lv2 in data[lv1]:
#     temp = data[lv1][lv2]
#     print(temp)
#     m = routerModel(lv2,temp['date'],temp['angle_id'],temp['status'], temp['predict_result'])
#     ob1.append(m)
#   listData.append(ob1)

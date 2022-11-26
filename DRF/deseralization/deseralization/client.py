import requests
import json
BASE_URL = 'http://127.0.0.1:8000/stud'

data = {
    "name":'sharif',
    "roll":101,
    "city":'Pune'
}

json_data = json.dumps(data)
res = requests.post(url=BASE_URL,data=json_data)
data1 = res.json()
print(data1)
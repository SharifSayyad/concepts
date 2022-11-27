import requests
import json
BASE_URL = 'http://127.0.0.1:8000/stud/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {"id":id}
    json_data = json.dumps(data)
    res = requests.get(url=BASE_URL,data=json_data)
    data = res.json()
    print(data)
# get_data()

def post_data():
    data = {
        'name':'XXX',
        'roll':102,
        'city': 'Kholapur'
    }
    json_data = json.dumps(data)
    res = requests.post(url=BASE_URL,data=json_data)
    data = res.json()
    print(data)
# post_data()

def update_data():
    data = {
        'id':2,
        'roll':111,
        'name':'CBV',
        'city':'satara'
    }
    json_data = json.dumps(data)
    res = requests.put(url=BASE_URL,data=json_data)
    data = res.json()
    print(data)
# update_data()

def delete_data():
    data = {"id":1}
    json_data = json.dumps(data)
    res = requests.delete(url=BASE_URL,data=json_data)
    data = res.json()
    print(data)
# delete_data()

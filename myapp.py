import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"
def get_data(id = None):
    data={}
    if id is not None:
        data = {'id':id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    response = requests.get(url=URL, headers=headers,data=json_data)
    data=response.json()
    print(data)

#get_data()

def post_data():
    data = {
        'name': 'Chaman Pandey',
        'roll': 106,
        'city': 'Buxar'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

post_data()

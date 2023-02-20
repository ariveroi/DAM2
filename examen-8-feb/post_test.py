import requests
import json

my_data = {
        'username': 'agustin',
        'password': '1234'
    }

req = requests.post('http://127.0.0.1:5001/login', data=json.dumps(my_data))

print(req)
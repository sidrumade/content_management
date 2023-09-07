import requests
import json

url = 'http://localhost:8000/authors'

payload = {
    'email': 'johndoe@example.com',
    'password': 'password123',
    'fullname': 'John Doe',
    'phone': '9876543210',
    'address': '123 Main Street',
    'city': 'Anytown',
    'state': 'CA',
    'country': 'USA',
    'pincode': '123456',
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

if response.status_code == 201:
    print('Author created successfully')
else:
    print(response.content)
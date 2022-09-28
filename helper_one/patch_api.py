import requests
import json
import jsonpath

endpoint_url ="https://reqres.in/api/users/2" #"https://reqres.in/api/users?page=2"

payload = {
    "name": "Vijaykumar",
    "job": "Automation leader"
}

resp = requests.patch(endpoint_url,payload)
print(resp.status_code)
print(resp.json())
print(requests.get(endpoint_url).json())




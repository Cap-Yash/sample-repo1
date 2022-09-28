import requests
import json
import jsonpath

endpoint_url ="https://reqres.in/api/users/2" #"https://reqres.in/api/users?page=2"

resp = requests.delete(endpoint_url)
print(resp.status_code)
print(resp.json())
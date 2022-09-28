import requests
import json
import jsonpath

endpoint_url ="https://reqres.in/api/users?page=2"

response = requests.get(endpoint_url)
# print (response)
# print(type(response))
assert response.status_code == 200
print(response.content)
content = response.json()["data"]

print(content)
print(response.json()["data"][0]["id"])



import requests
import json
import os



url = "https://httpbin.org/get"
#"https://httpbin.org/patch"
    #"https://httpbin.org/basic-auth/{user}/{passwd}" #"https://httpbin.org/post"

params = {"user":"abcd", "passwd": "abcd"}
#response = requests.post("https://httpbin.org/post")

def get_method(url, *args):
    resp = requests.get(url, params=args)
    return resp

response1 = get_method(url, params)
endpoint_url ="https://reqres.in/api/users?page=2"
response = get_method(endpoint_url)
#response = requests.put(url)

print (response.status_code)
print (response.json())
print (response.text)
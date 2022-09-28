# import requests
# import json
# import jsonpath
#
# endpoint_url ="https://reqres.in/api/users" #"https://reqres.in/api/users?page=2"
# payload = {
#     "name": "Vijaykumar1",
#     "job": "leader"
# }
#
# resp = requests.post(endpoint_url,payload)
# print(resp.status_code)
# print(resp.json())
#
# post_id = resp.json()["id"]
#
# req_get = requests.get("https://reqres.in/api/users/7")
# assert post_id!=req_get

import requests

url = "https://voicerss-text-to-speech.p.rapidapi.com/"

querystring = {"key":"undefined"}

payload = "src=Hello%2C%20world!&hl=en-us&r=0&c=mp3&f=8khz_8bit_mono"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "voicerss-text-to-speech.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

import requests
import json
import os
import time

class CRUD:

    def get_method(endpoint_url):
        response = requests.get(endpoint_url)
        return response

    def post_method(endpoint_url, payload):
        response = requests.post(endpoint_url, payload)
        return response


    def put_method(endpoint_url, payload):
        response = requests.put(endpoint_url, payload)
        return response


    def patch_method(endpoint_url, payload):
        response = requests.patch(endpoint_url, payload)
        return response


    def del_method(endpoint_url):
        response = requests.delete(endpoint_url)
        return response


    def validate_response(response, value1, value):
        data = response.json()[value1]
        assert data == value

    def validate_status_code(response,value):
        if response.status_code == value:
            assert True
        else:
            assert False


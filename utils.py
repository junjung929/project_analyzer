import requests
import json
# Extract to csv
# Requests


def get(url, api, auth=None):
    endpoint = url + api
    try:
        response = requests.request("GET", endpoint, auth=auth)
        return json.loads(response.text)
    except Exception as e:
        print(e)
        return -1

def post(url, api, params={}, auth=None):
    endpoint = url + api
    try:
        response = requests.request("POST", endpoint, auth=auth, params=params)
        return json.loads(response.text)
    except Exception as e:
        print(e)
        return -1

def getBasicAuth(username, password):
    return requests.auth.HTTPBasicAuth(username, password)
# Convert to JSON

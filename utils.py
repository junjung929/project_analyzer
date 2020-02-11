import requests
import json
import os
# Extract to csv
# Requests
ENV = os.environ.get("ENV") or "development"


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

def getConfig(target):
    if ENV == "development":
        config_path = "config.test.json"
    else:
        config_path = "config.json"
    
    with open(config_path) as config_data:
        config = json.load(config_data)
    return config.get(target)
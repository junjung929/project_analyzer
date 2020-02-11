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
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(e)


def post(url, api, params={}, auth=None):
    endpoint = url + api
    try:
        response = requests.request("POST", endpoint, auth=auth, params=params)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(e)


def getBasicAuth(username, password):
    return requests.auth.HTTPBasicAuth(username, password)


def getConfig(target):
    config_path = "config.test.json" if ENV == "development" else "config.json"
    try:
        with open(config_path) as config_data:
            config = json.load(config_data)
        return config.get(target)
    except Exception as e:
        raise Exception(e)

import requests
import json
import os
import csv

ENV = os.environ.get("ENV") or "development"
CONFIG_PATH = "config.test.json" if ENV == "development" else "config.json"


def get(url, api, auth=None, params={}):
    endpoint = url + api
    try:
        response = requests.request("GET", endpoint, auth=auth, params=params)
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
    try:
        with open(CONFIG_PATH) as config_data:
            config = json.load(config_data)
        return config.get(target) or {}
    except Exception as e:
        raise Exception(e)


def extractAnalysisToCSV(filename, data):
    heads = [
        'projectName', 'creationDate', 'creationCommitHash', 'type', 'squid', 'component',
        'severity', 'startLine', 'endLine', 'resolution', 'status', 'message',
        'effort', 'debt', 'author']
    try:
        with open("analysis_results/"+filename+".csv", "w") as analysis_file:
            writer = csv.writer(analysis_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(heads)

            for row in data:
                writer.writerow([
                    row.get("project") or "",
                    row.get("creationDate") or "",
                    row.get("hash") or "",
                    row.get("type") or "",
                    row.get('rule') or "",
                    row.get('component') or "",
                    row.get('severity') or "",
                    row.get('textRange').get('startLine') or "",
                    row.get('textRange').get('endLine') or "",
                    row.get('resolution') or "",
                    row.get('status') or "",
                    row.get('message') or "",
                    row.get('effort') or "",
                    row.get('debt') or "",
                    row.get('author') or "",
                ])
        print("Analysis results successfully extracted to path: " +
              os.path.realpath("analysis_results/"+filename+".csv"))
    except Exception as e:
        print(e)

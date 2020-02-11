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


def extractAnalysisToCSV(filename, issues):
    heads = [
        'projectName', 'creationDate', 'creationCommitHash', 'type', 'squid', 'component',
        'severity', 'startLine', 'endLine', 'resolution', 'status', 'message',
        'effort', 'debt', 'author']
    try:
        with open("analysis_results/"+filename+".csv", "w") as analysis_file:
            writer = csv.writer(analysis_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(heads)

            for issue in issues:
                
                writer.writerow([
                    issue.get("project") or "",
                    issue.get("creationDate") or "",
                    issue.get("hash") or "",
                    issue.get("type") or "",
                    issue.get('rule') or "",
                    issue.get('component') or "",
                    issue.get('severity') or "",
                    issue.get('textRange').get('startLine') if issue.get('textRange') else "",
                    issue.get('textRange').get('endLine') if issue.get('textRange') else "",
                    issue.get('resolution') or "",
                    issue.get('status') or "",
                    issue.get('message') or "",
                    issue.get('effort') or "",
                    issue.get('debt') or "",
                    issue.get('author') or "",
                ])
        
    except Exception as e:
        print(e)


def extractCommitsToCSV(filename, commits):
    heads = [
        "projectID", "commitHash", "commitMessage", "author", "authorDate",
        "authorTimezone", "committer", "committerDate", "committerTimezone",
        "branches", "inMainBranch", "merge", "parents"
    ]
    try:
        with open("commit_data/"+filename+".csv", "w") as analysis_file:
            writer = csv.writer(analysis_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(heads)

            for commit in commits:
                writer.writerow([
                    commit.project_name or "",
                    commit.hash or "",
                    commit.msg or "",
                    commit.author.name or "",
                    commit.author_date or "",
                    commit.author_timezone or "",
                    commit.committer.name or "",
                    commit.committer_date or "",
                    commit.committer_timezone or "",
                    commit.branches or "",
                    commit.in_main_branch or "",
                    commit.merge or "",
                    commit.parents or "",
                ])

    except Exception as e:
        print(e)

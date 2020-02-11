import os
import requests
import json
import utils

ENV = os.environ.get("ENV") or "development"

if ENV == "development":
    CONFIG_PATH = "config.test.json"
else:
    CONFIG_PATH = "config.json"

with open(CONFIG_PATH) as config_data:
    config = json.load(config_data)
    sonar = config.get("sonar")
    default_server = sonar.get("server_url")
    username = sonar.get("username")
    password = sonar.get("password")
    token = sonar.get("token")

SERVER_NOT_RUNNING = False
SERVER_IS_RUNNING = True


class SonarHelper:
    def __init__(self, url=default_server):
        self.token_name = None
        self.token = token
        self.server_url = url
        self.basicAuth = None

    # Check connection
    def checkConnection(self):
        res = utils.get(self.server_url, "/api/system/status")
        status = res.get("status")
        if status == "UP":
            return SERVER_IS_RUNNING
        elif status == "STARTING":
            print("Server is starting. Please wait a while and try again")
            return SERVER_NOT_RUNNING
        else:
            print("Please make sure your Sonarqube server is running on '"
                  + self.server_url+"'")
            return SERVER_NOT_RUNNING

    # Authenticate
    def auth(self):
        self.basicAuth = utils.getBasicAuth(username, password)

    # Generate token
    def generateToken(self):
        if self.basicAuth is None:
            self.auth()
        if self.token_name is None:
            self.token_name = input("Please input the token name: ")

        querystring = {"name": self.token_name}
        res = utils.post(
            self.server_url, "/api/user_tokens/generate", querystring, self.basicAuth)

        if res.get("errors"):
            for error in res.get("errors"):
                print("Error: " + error.get("msg"))
        self.token = res.get("token")

    def analyze(self, basename):
        try:
            os.system("cd " + basename + " && mvn clean compile sonar:sonar -Dsonar.host.url=" +
                      self.server_url+" -Dsonar.login=" + self.token)
        except Exception as e:
            print(e)
    # Run analysis maven

    # Get issues

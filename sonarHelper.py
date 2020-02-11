import os
import requests
import json
import utils

config = utils.getConfig("sonar")
default_server = config.get("server_url") or None
username = config.get("username") or None
password = config.get("password") or None
tokenname = config.get("tokenname") or None

SERVER_NOT_RUNNING = False
SERVER_IS_RUNNING = True


class SonarHelper:
    def __init__(self, url=default_server, name=None):
        self.token_name = tokenname
        self.token = None
        self.server_url = url
        self.basicAuth = None
        self.key = None
        self.name = name

    # Check connection
    def checkConnection(self):
        try:
            res = utils.get(self.server_url, "/api/system/status")
        except Exception:
            print("\nError: Cannot connect the Sonarqube server. Please make sure your Sonarqube server is running on '"
                  + self.server_url+"'")
            return SERVER_NOT_RUNNING
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
        try:
            res = utils.post(
                self.server_url, "/api/user_tokens/generate", querystring, self.basicAuth)

            if res.get("errors"):
                for error in res.get("errors"):
                    print("Error: " + error.get("msg"))
                raise Exception("Cannot generate token")
            self.token = res.get("token")
        except Exception as e:
            self.token_name = None
            self.generateToken()

    def getKey(self):
        res = utils.get(self.server_url, '/api/projects/search',
                        self.basicAuth, {"q": self.name})
        compo = res.get("components")
        self.key = compo[0].get("key")

    # Run analysis maven
    def analyze(self, basename):
        try:
            if self.token is None:
                self.generateToken()
            os.system("cd " + basename + " && mvn clean compile sonar:sonar -Dsonar.host.url=" +
                      self.server_url+" -Dsonar.login=" + self.token)
        except Exception as e:
            raise Exception(e)

    # Get issues
    def getIssues(self):
        print("Extracting issues...")
        if self.basicAuth is None:
            self.auth()
        if self.key is None:
            self.getKey()
        try:
            res = utils.get(self.server_url,
                            '/api/issues/search', self.basicAuth, {"componentKeys": self.key})

            if res.get("errors"):
                for error in res.get("errors"):
                    print("Error: " + error.get("msg"))
                raise Exception("Cannot get issues")

            issues = res.get("issues")

            utils.extractAnalysisToCSV(self.name, issues)
            print("Analysis results successfully extracted to path: " +
                  os.path.realpath("analysis_results/"+self.name+".csv"))

        except Exception as e:
            raise Exception(e)

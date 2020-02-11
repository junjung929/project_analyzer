import requests
import json

class SonarHelper:
    def __init__(self):
        self.username = None
        self.password = None
        self.tokenname = None
        self.token = None
    
    # Check connection

    # Authenticate
    def auth(self):
        self.username = input(
            "Please input your username for Sonarqube(default is 'admin'): ") or "admin"
        self.password = input(
            "Please input your password for Sonarqube(default is 'admin'): ") or "admin"
        self.basicAuth = requests.auth.HTTPBasicAuth(self.username, self.password)
    
    # Get token

    # Run analysis maven

    # Get issues
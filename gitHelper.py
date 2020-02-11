import os
from git import Repo
import utils

config = utils.getConfig("git")
default_project = config.get("project_url") or None
default_name = config.get("project_name") or None


class GitHelper():
    def __init__(self, url=default_project, name=default_name):
        self.url = url
        self.name = name
        self.cloned_repo = None
        self.setProject()

    # Ask URL
    def setProject(self):
        if self.name is None or self.url is None:
            self.url = input(
                "\nPlease give the full URL address of the JAVA project you want to analyze: ")
            self.name = os.path.basename(self.url).split(".")[0]
            self.path = "projects/" + self.name
            self.cloneRepository()

        else:
            print("\nCurrent project is set '" + self.name + "'")
            self.path = "projects/" + self.name
            while True:
                isChange = input("Would you like to analyze another project?(y/N): ") or "n"
                if isChange is "y" or isChange is "Y":
                    self.resetProject()
                    self.setProject()
                    print("Current project is set '" + self.name + "'")
                    break
                elif isChange is "n" or isChange is "N":
                    break
        self.cloned_repo = Repo(self.path)

    def resetProject(self):
        self.url = None
        self.name = None
        self.cloned_repo = None

    # Clone repository
    def cloneRepository(self):
        if self.name is None:
            return self.setProject()
        if os.path.isdir(self.path):
            # Check existance of the repo
            print("\nThe repository '" + self.name + "' already exists.")
            # self.cloned_repo = Repo(self.path)
            # print("Update the repository...")
            # self.cloned_repo.remotes.origin.pull()
            # print("Update done")
        else:
            try:
                print("\nCloning '" + self.name+"' respository...")
                Repo.clone_from(self.url, self.path)
                print("The repository is successfully cloned")
            except Exception as e:
                # Fail
                print(e)
                return -1

    # Get commits

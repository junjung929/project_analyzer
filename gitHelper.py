import os
from git import Repo


class GitHelper():
    def __init__(self, url=None, name=None):
        self.url = url
        self.name = name
        self.cloned_repo = None

    # Ask URL
    def setProject(self):
        if self.name is None:
            self.url = input(
                "Please give the full URL address of the JAVA project you want to analyze: ")
            self.name = os.path.basename(self.url).split(".")[0]
            self.cloneRepository()

        else:
            isChange = input("Would you like to analyze another project? (current project '"
                             + self.name
                             
                             + "')(y/N)") or False
            if isChange is not False:
                self.resetProject()
                self.setProject()
            
    def resetProject(self):
        self.url = None
        self.name = None
        self.cloned_repo = None

    # Clone repository
    def cloneRepository(self):
        if self.name is None:
            return self.setProject()
        path = "projects/" + self.name
        if os.path.isdir(path):
            # Check existance of the repo
            print("The repository '" + self.name + "' already exists.")
        else:
            try:
                print("Cloning '" + self.name+"' respository...")
                Repo.clone_from(self.url, path)
                print("The repository is successfully cloned")
                self.cloned_repo = Repo(path)
            except Exception as e:
                # Fail
                print(e)
                return -1 

    # Get commits

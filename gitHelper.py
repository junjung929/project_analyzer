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
                "\nPlease give the full URL address of the JAVA project you want to analyze: ")
            self.name = os.path.basename(self.url).split(".")[0]
            self.cloneRepository()

        else:
            while True:
                isChange = input("\nWould you like to analyze another project? (current project '"
                                 + self.name
                                 + "')(y/N): ") or "n"
                if isChange is "y" or isChange is "Y":
                    self.resetProject()
                    self.setProject()
                    break
                elif isChange is "n" or isChange is "N":
                    break
        print("Current project is '" + self.name + "'")

    def resetProject(self):
        self.url = None
        self.name = None
        self.cloned_repo = None

    # Clone repository
    def cloneRepository(self):
        if self.name is None:
            return self.setProject()
        self.path = "projects/" + self.name
        if os.path.isdir(self.path):
            # Check existance of the repo
            print("\nThe repository '" + self.name + "' already exists.")
            self.cloned_repo = Repo(self.path)
            print("Update the repository...")
            self.cloned_repo.remotes.origin.pull()
            print("Update done")
        else:
            try:
                print("\nCloning '" + self.name+"' respository...")
                Repo.clone_from(self.url, self.path)
                print("The repository is successfully cloned")
                self.cloned_repo = Repo(self.path)
            except Exception as e:
                # Fail
                print(e)
                return -1

    # Get commits

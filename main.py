from gitHelper import GitHelper
from sonarHelper import SonarHelper

def main():
    project = GitHelper()
    sonar = SonarHelper()
    while True:
        project.setProject()
        print("\n####################################")
        print("1. Sonarqube")
        print("q. Quit")
        print("####################################")
        select = input("Choose a tool to analyze: ")
        if select == "q":
            print("Finishing the program...")
            exit(0)
        elif select == "1":
            if sonar.checkConnection():
                # connection succeed
                sonar.generateToken()
                sonar.analyze(project.path)
        else:
            print("Please give a valid option from the list")
            pass


if __name__ == "__main__":
    main()

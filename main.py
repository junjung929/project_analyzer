from gitHelper import GitHelper
from sonarHelper import SonarHelper

project = GitHelper()
sonar = SonarHelper()

def main():
    while True:
        print("\n#################################################")
        print("1. Analyze a JAVA project via Sonarqube")
        print("q. Quit")
        print("#################################################")
        select = input("Choose an option above: ")
        if select == "q" or select == "Q":
            print("\nFinishing the program...")
            exit(0)
        elif select == "1":
            print("\nSelected option: Analyze a JAVA project via Sonarqube")
            if sonar.checkConnection():
                # connection succeed
                project.setProject()
                # sonar.getIssues()
                sonar.analyze(project.path)
        else:
            print("Please give a valid option from the list")
            pass


if __name__ == "__main__":
    main()

from gitHelper import GitHelper
from sonarHelper import SonarHelper



def main():
    while True:
        print("\n#################################################\n")
        print("1. Analyze a JAVA project via Sonarqube")
        print("2. Analyze a JAVA project via PMD")
        print("3. Analyze a JAVA project via Checkstyle")
        print("q. Quit")
        print("\n#################################################\n")
        select = input("Choose an option from above: ")
        if select == "q" or select == "Q":
            print("\nFinishing the program...")
            exit(0)
        elif select == "1":
            print("\nSelected option: Analyze a JAVA project via Sonarqube")
            project = GitHelper()
            sonar = SonarHelper(name=project.name)
            if sonar.checkConnection():
                # connection succeed
                try:
                    print("\nProcess analyzing...")
                    sonar.analyze(project.path)
                    print("\nProcess extracting...")
                    sonar.getIssues()
                    project.getCommits()
                    print("\nAnalyzing successfully done!")
                except Exception as e:
                    print(e)
        elif select == "2":
            print("\nSelected option is not available yet")
        elif select == "3":
            print("\nSelected option is not available yet")
        else:
            print("\nWrong option. Please give a valid option from the list")
            pass


if __name__ == "__main__":
    main()

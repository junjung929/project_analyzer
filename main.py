from gitHelper import GitHelper

def main():
    project = GitHelper()
    project.setProject()

    # while True:
    #     print("1. Analyze a JAVA project via Sonarqube")
    #     print("q. Quit")
    #     select = input("Choose an option: ")
    #     if select == "q":
    #         print("Finishing the program...")
    #         exit(0)
    #     elif select == "1":
    #         print('sonar analysis')
    #     else:
    #         pass


if __name__ == "__main__":
    main()

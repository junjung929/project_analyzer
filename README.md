# Analyze JAVA projects via multiple tools

## Install

```bash
# Clone the repository
git clone <repo_url> <dir_name>
cd <dir_name>

# Install dependancies
pip3 install requirements.txt

# Run the program in development mode
python3 main.py

# Run the program in production mode
ENV=prod python3 main.py
```

## Configuration


Configuration file for testing is located at [config.text.json](config.test.json).

For production, copy the test.json file and change credentials.

## Analyze JAVA project via Sonarqube

This program analyzes JAVA projects using maven

* Run the sonarcube server

    ```docker run -d --name sonarqube -p 9000:9000 sonarqube:7.5-community```

* Run the program

    * in test mode
    
        ```python3 main.py```

    * in production mode
    
        ```ENV=prod python3 main.py```

* Choose first option

## Analyze JAVA project via PDM

Under development

## Analyze JAVA project via Checkstyle

Under development


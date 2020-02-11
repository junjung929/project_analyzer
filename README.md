# Analyze JAVA projects via multiple tools

This program is to analyze projects written in JAVA using three different analyzing tools; Sonarqube, PDM and Checkstyle.
In result, it extracts issues and commits into CSV files.

## Install

```bash
# Clone the repository
git clone https://github.com/junjung929/project_analyzer.git project_analyzer
cd project_analyzer

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


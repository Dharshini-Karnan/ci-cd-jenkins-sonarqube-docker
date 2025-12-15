pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                bat '''
                C:\\Users\\dhars\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m tests.test_app
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat '''
                    sonar-scanner
                    '''
                }
            }
        }
    }
}

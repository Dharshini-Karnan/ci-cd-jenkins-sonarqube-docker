pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                powershell '''
                python -m tests.test_app
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    powershell '''
                    sonar-scanner
                    '''
                }
            }
        }
    }
}


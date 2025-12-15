pipeline {
    agent any

    stages {

        stage('Test') {
            steps {
                bat '''
                python -m tests.test_app
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


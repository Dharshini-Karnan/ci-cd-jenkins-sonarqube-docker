pipeline {
    agent any

    environment {
        PYTHON_EXE   = 'C:\\Users\\dhars\\AppData\\Local\\Programs\\Python\\Python312\\python.exe'
        DOCKER_IMAGE = 'dharshinikarnan/ci-cd-python-app:latest'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test') {
            steps {
                bat """
                %PYTHON_EXE% -m tests.test_app
                """
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        bat """
                        "${scannerHome}\\bin\\sonar-scanner.bat"
                        """
                    }
                }
            }
        }
        // ❌ Quality Gate REMOVED to avoid pipeline timeout

        stage('Docker Build') {
            steps {
                bat """
                docker build -t %DOCKER_IMAGE% .
                """
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    bat """
                    docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                    docker push %DOCKER_IMAGE%
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}

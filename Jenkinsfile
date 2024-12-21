pipeline {
  agent any
  
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub_id')
  }
    stages {
        stage('Clone Git Repository') {
            steps {
                script {
                    sh 'rm -rf dev-week'
                    checkout scm // checkout based on the configured credentials in the current Jenkins Job
                    sh 'pwd'
                }
            }
        }

        stage('Unit Test') {
            steps {
                sh '''
                    source ${SHELL_PATH}
                    ${POETRY_PATH} install
                    ${PYTEST_PATH} tests/test_calculator.py
                '''
            }
        }
       
        // stage('Linting') {
        //     steps {
        //         sh '${FLAKE8_PATH} tests'
        //     }    
        // }

        stage('Build Image') {
            steps {
                sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | sudo "${DOCKER_PATH}" login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    sudo "${DOCKER_PATH}" build -t "${REGISTRY}":"${BUILD_NUMBER}" .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo "${DOCKER_PATH}" login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        
        stage('Push To DockerHub') {
            steps {
                sh 'sudo "${DOCKER_PATH}" push "${REGISTRY}":"${BUILD_NUMBER}"'
                
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'sudo "${DOCKER_PATH}" run -d --restart unless-stopped -p 5002:5002 "${REGISTRY}":"${BUILD_NUMBER}"'
                }
            }
        }    
    }
}
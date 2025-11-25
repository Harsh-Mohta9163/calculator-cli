pipeline {
    agent any

    environment {
        IMAGE = "harsh9163/imt2023106:jenkins"
        VENV = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                  branches: [[name: '*/master']],
                  userRemoteConfigs: [[
                    url: 'https://github.com/Harsh-Mohta9163/calculator-cli.git',
                    credentialsId: 'github-creds'
                  ]]
                ])
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\python.exe -m pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '%VENV%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '%VENV%\\Scripts\\pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE% .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    bat '''
                      echo %PASS% | docker login -u %USER% --password-stdin
                      docker push %IMAGE%
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                bat '''
                  docker pull %IMAGE%
                  docker stop calculator-cli || exit 0
                  docker rm calculator-cli || exit 0
                  docker run -d --name calculator-cli %IMAGE%
                '''
            }
        }
    }
}

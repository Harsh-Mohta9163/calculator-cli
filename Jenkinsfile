pipeline {
    agent any

    environment {
        IMAGE = "harsh9163/calculator-cli:jenkins"
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
                sh '$PYTHON -m venv $VENV'
                sh '$VENV/bin/pip install --upgrade pip'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '$VENV/bin/pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                                                  usernameVariable: 'USER',
                                                  passwordVariable: 'PASS')]) {
                    sh '''
                      echo $PASS | docker login -u $USER --password-stdin
                      docker push $IMAGE
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                  docker pull $IMAGE
                  docker stop calculator-cli || true
                  docker rm calculator-cli || true
                  docker run -d --name calculator-cli $IMAGE
                '''
            }
        }
    }
}

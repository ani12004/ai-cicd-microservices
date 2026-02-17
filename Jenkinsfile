pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build AI Image') {
            steps {
                sh 'docker build -t ai-module ./ai-module'
            }
        }

        stage('Run AI Prioritization') {
            steps {
                sh 'docker run --rm -v $PWD/ai-module:/app ai-module'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install pytest'
                sh 'pytest user-service'
                sh 'pytest product-service'
                sh 'pytest order-service'
                sh 'pytest payment-service'
            }
        }

        stage('Build & Deploy Microservices') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}

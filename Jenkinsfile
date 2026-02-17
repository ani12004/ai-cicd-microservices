pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/ani12004/ai-cicd-microservices.git"
        PROJECT_DIR = "ai-cicd-microservices"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Train AI Model') {
            steps {
                dir('ai-module') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'python3 train_model.py'
                }
            }
        }

        stage('Generate Test Priorities') {
            steps {
                dir('ai-module') {
                    sh 'python3 predict_priority.py'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run Service Tests') {
            steps {
                dir('user-service') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest test_user.py'
                }
                dir('product-service') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest test_product.py'
                }
                dir('order-service') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest test_order.py'
                }
                dir('payment-service') {
                    sh 'pip3 install -r requirements.txt'
                    sh 'pytest test_payment.py'
                }
            }
        }

        stage('Deploy Services') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        success {
            echo "Pipeline Completed Successfully 🚀"
        }
        failure {
            echo "Pipeline Failed ❌"
        }
    }
}

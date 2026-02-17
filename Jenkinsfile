pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/ani12004/ai-cicd-microservices.git"
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
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        python train_model.py
                    '''
                }
            }
        }

        stage('Generate Test Priorities') {
            steps {
                dir('ai-module') {
                    sh '''
                        . venv/bin/activate
                        python predict_priority.py
                    '''
                }
            }
        }

        stage('Run Service Tests') {
            steps {
                sh '''
                    python3 -m venv testenv
                    . testenv/bin/activate
                    pip install --upgrade pip
                    pip install pytest

                    pip install -r user-service/requirements.txt
                    pip install -r product-service/requirements.txt
                    pip install -r order-service/requirements.txt
                    pip install -r payment-service/requirements.txt

                    pytest user-service/test_user.py
                    pytest product-service/test_product.py
                    pytest order-service/test_order.py
                    pytest payment-service/test_payment.py
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
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
            echo "✅ Pipeline Completed Successfully 🚀"
        }
        failure {
            echo "❌ Pipeline Failed"
        }
    }
}

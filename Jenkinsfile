pipeline {
    agent any

    environment {
        PROJECT_DIR = "/var/jenkins_home/workspace/AI-CICD-Microservices"
        VENV_DIR = "${PROJECT_DIR}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ani12004/ai-cicd-microservices.git'
            }
        }

        stage('Setup Python Virtual Environment') {
            steps {
                sh """
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r ${PROJECT_DIR}/ai-module/requirements.txt
                """
            }
        }

        stage('Build Microservices') {
            steps {
                sh "docker build -t order-service ${PROJECT_DIR}/order-service"
                sh "docker build -t user-service ${PROJECT_DIR}/user-service"
                sh "docker build -t product-service ${PROJECT_DIR}/product-service"
                sh "docker build -t payment-service ${PROJECT_DIR}/payment-service"
            }
        }

        stage('AI Test Prioritization') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    python3 ${PROJECT_DIR}/ai-module/predict_priority.py
                """
            }
        }

        stage('Run Prioritized Tests') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    python3 ${PROJECT_DIR}/order-service/test_order.py
                    python3 ${PROJECT_DIR}/user-service/test_user.py
                    python3 ${PROJECT_DIR}/product-service/test_product.py
                    python3 ${PROJECT_DIR}/payment-service/test_payment.py
                """
            }
        }

        stage('Optional: Deploy Services') {
            steps {
                sh "docker run -d --name order-service order-service || true"
                sh "docker run -d --name user-service user-service || true"
                sh "docker run -d --name product-service product-service || true"
                sh "docker run -d --name payment-service payment-service || true"
            }
        }
    }

    post {
        always {
            echo "Pipeline finished. Check test results and running containers."
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}

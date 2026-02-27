pipeline {
    agent any

    environment {
        PROJECT_DIR = "/mnt/d/downloads/project-mid/ai-cicd-microservices"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ani12004/ai-cicd-microservices.git'
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh "pip install -r ${PROJECT_DIR}/ai-module/requirements.txt"
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
                sh "python3 ${PROJECT_DIR}/ai-module/predict_priority.py"
            }
        }

        stage('Run Prioritized Tests') {
            steps {
                sh "python3 ${PROJECT_DIR}/order-service/test_order.py"
                sh "python3 ${PROJECT_DIR}/user-service/test_user.py"
                sh "python3 ${PROJECT_DIR}/product-service/test_product.py"
                sh "python3 ${PROJECT_DIR}/payment-service/test_payment.py"
            }
        }

        stage('Optional: Deploy Services') {
            steps {
                sh "docker run -d --name order-service order-service"
                sh "docker run -d --name user-service user-service"
                sh "docker run -d --name product-service product-service"
                sh "docker run -d --name payment-service payment-service"
            }
        }
    }
}

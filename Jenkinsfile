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
                    apt update || true
                    apt install -y python3-venv python3-pip || true
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
                    cd ${PROJECT_DIR}/ai-module
                    python3 predict_priority.py
                """
            }
        }

        stage('Run Prioritized Tests') {
            steps {
                sh """
                    source ${VENV_DIR}/bin/activate
                    cd ${PROJECT_DIR}/order-service
                    python3 test_order.py

                    cd ${PROJECT_DIR}/user-service
                    python3 test_user.py

                    cd ${PROJECT_DIR}/product-service
                    python3 test_product.py

                    cd ${PROJECT_DIR}/payment-service
                    python3 test_payment.py
                """
            }
        }

        stage('Optional: Deploy Services') {
            steps {
                sh """
                    # Cleanup old containers if they exist
                    docker rm -f order-service || true
                    docker rm -f user-service || true
                    docker rm -f product-service || true
                    docker rm -f payment-service || true

                    # Deploy containers
                    docker run -d --name order-service order-service
                    docker run -d --name user-service user-service
                    docker run -d --name product-service product-service
                    docker run -d --name payment-service payment-service
                """
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

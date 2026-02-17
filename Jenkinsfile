pipeline {
    agent any

    stages {

        stage('Install Python Dependencies') {
            steps {
                sh 'pip install pytest pandas scikit-learn joblib'
            }
        }

        stage('Train AI Model') {
            steps {
                sh 'cd ai-module && python3 train_model.py'
            }
        }

        stage('AI Test Prioritization') {
            steps {
                sh 'cd ai-module && python3 predict_priority.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest user-service'
                sh 'pytest product-service'
                sh 'pytest order-service'
                sh 'pytest payment-service'
            }
        }

        stage('Build & Deploy') {
            steps {
                sh 'docker-compose up --build -d'
            }
        }
    }
}

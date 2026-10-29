pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-app .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat '''
                docker rm -f student-app-container 2>NUL
                docker run -d --name student-app-container -p 5000:5000 student-app
                '''
            }
        }

        stage('Health Check') {
            steps {
                bat 'curl.exe -f http://localhost:5000/health'
            }
        }
    }
}
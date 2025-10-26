pipeline {
    agent { docker { image 'python:3.11-slim' } }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest test_app.py -v'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deployment successful'
            }
        }
    }
}
pipeline {
    agent any

    environment {
        // Jenkins can't find Homebrew's python3 without this
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Environment') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Run Tests') {
            steps {
                // build fails if any test fails
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
    }

    post {
        success {
            echo 'Build passed'
        }
        failure {
            echo 'Build failed'
        }
    }
}

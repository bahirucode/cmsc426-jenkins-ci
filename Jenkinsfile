// Declarative pipeline for the CMSC 426 CI activity.
// Jenkins pulls this file from GitHub ("Pipeline script from SCM") and runs it.
pipeline {
    agent any

    environment {
        // Jenkins started by `brew services` only gets /usr/bin:/bin:/usr/sbin:/sbin,
        // so put Homebrew first to use the same python3 as my terminal.
        PATH = "/opt/homebrew/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Environment verification') {
            steps {
                sh 'which python3'
                sh 'python3 --version'
                sh 'git --version'
            }
        }

        stage('Run app') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Unit tests') {
            steps {
                // A failing test exits non-zero, which marks the build as FAILURE.
                sh 'python3 -m unittest discover -s tests -v'
            }
        }
    }

    post {
        success {
            echo 'Build succeeded: the app ran and all unit tests passed.'
        }
        failure {
            echo 'Build failed: check the console output above for the failing stage or test.'
        }
    }
}

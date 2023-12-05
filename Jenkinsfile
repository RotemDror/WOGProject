pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/RotemDror/WOGProject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('E2E Tests') {
            steps {
                script {
                    def e2eExitCode = sh(script: 'python e2e.py', returnStatus: true)
                    
                    if (e2eExitCode != 0) {
                        error 'E2E tests failed.'
                    }
                }
            }
        }

        stage('Push Docker Compose Images') {
            when {
                expression { currentBuild.resultIsBetterOrEqualTo('SUCCESS') }
            }
            steps {
                script {
                    sh 'docker-compose push'
                }
            }
        }

        stage('Stop Docker Compose') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }
}

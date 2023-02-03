
pipeline {
    agent any
    
    stages {
        stage('Checkout Repository') {
            steps {
                git 'https://github.com/saleemgdn/World_of_Games.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t games_docker_image .'
            }
        }
        stage('Run Docker Application') {
            steps {
                sh 'docker run -p 8777:8777 games_docker_image'
            }
        }
        stage('Run e2e.py') {
            steps {
                sh 'e2e.py'
            }
            post {
                success {
                    script {
                        if(fileExists('e2e.py')) {
                            if (sh(script: 'e2e.py', returnStatus: true) == 0) {
                                echo 'Tests passed'
                            } else {
                                echo 'Tests failed'
                            }
                        }
                    }
                }
            }
        }
        stage('Terminate Container and Push to Docker Hub') {
            steps {
                sh 'docker stop $(docker ps -q)'
                sh 'docker push samo3889/scores_app'
            }
        }
    }
}
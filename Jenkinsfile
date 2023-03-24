pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('Scores') {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                dir('Scores') {
                    sh 'docker-compose up -d'

                }
            }
        }

        stage('Test') {
            steps {
                dir('tests') {
                    sh 'python3 e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                dir('Scores') {
                    sh 'docker-compose down'
                    sh 'docker-compose push'
                }
            }
        }
    }
}

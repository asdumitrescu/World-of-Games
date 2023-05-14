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
                    sh 'docker-compose exec -it flask_app python3 e2e.py'
                }
            }
        }
        stage('Finalize') {
            steps {
                withCredentials([usernamePassword(credentialsId: '64ff5082-093b-4a8a-9547-117f113c544b', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    dir('Scores') {
                        sh 'docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}'
                        sh 'docker-compose down'
                        sh 'docker-compose push'
                    }
                }
            }
        }
    }
}

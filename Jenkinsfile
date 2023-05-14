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
                withCredentials([usernamePassword(credentialsId: '4d8ed3c0-10b3-48e8-b533-14530b2329ff', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    dir('Scores') {
                        sh "echo ${DOCKER_PASSWORD} | docker-compose exec -T flask_app sh -c 'docker login -u ${DOCKER_USERNAME} --password-stdin'"

                        sh 'docker-compose down'
                        sh 'docker-compose push'
                    }
                }
            }
        }
    }
}

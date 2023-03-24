pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Run') {
            steps {
                sh 'docker-compose up -d'
                sleep(time: 10, unit: 'SECONDS')
            }
        }

        stage('Test') {
            steps {
                sh 'python3 tests/e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                sh 'docker tag wog_scores_flask_jenkins asdumitrescu/wog_scores_flask_jenkins:latest'
                sh 'docker push asdumitrescu/wog_scores_flask_jenkins:latest'
            }
        }
    }

    post {
        always {
            sh 'docker-compose down --remove-orphans'
        }
    }
}

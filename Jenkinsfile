pipeline {
    agent any # Use any available agent to run the pipeline

    stages { # Define the stages in the pipeline
        stage('Build') { # First stage: Build
            steps {
                dir('Scores') { # Change to the 'Scores' directory
                    sh 'docker-compose build' # Build the Docker images defined in the docker-compose.yml file
                }
            }
        }

        stage('Run') { # Second stage: Run
            steps {
                dir('Scores') { # Change to the 'Scores' directory
                    sh 'docker-compose up -d' # Start the containers in detached mode (-d)
                }
            }
        }

        stage('Test') { # Third stage: Test
            steps {
                dir('tests') { # Change to the 'tests' directory
                    sh 'docker-compose exec flask_app python3 e2e.py'
                }
            }
        }
        stage('Finalize') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
                    dir('Scores') { # Change to the 'Scores' directory
                        sh 'docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_PASSWORD'
                        sh 'docker-compose down' # Stop and remove the containers
                        sh 'docker-compose push' Push the built images to a Docker registry
                    }
                }
            }
        }
    }
}

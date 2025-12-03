pipeline {
    agent any

    environment {
        AWS_REGION = 'ap-south-2'
        AWS_CREDENTIALS_ID = 'aws-calculator'
        STACK_NAME = 'calculator-stack'
        SAM_IMAGE = 'public.ecr.aws/sam/build-python3.12:latest'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Unit Tests (Docker)') {
            steps {
                bat """
                docker run --rm -v %WORKSPACE%:/app -w /app python:3.12 ^
                bash -c "pip install pytest && export PYTHONPATH=/app && pytest tests/ --junitxml=results.xml"
                """
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Build SAM package (Docker)') {
            steps {
                bat """
                docker run --rm -v %WORKSPACE%:/app -w /app %SAM_IMAGE% \
                    sam build
                """
            }
        }

        stage('Deploy to AWS (Docker)') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDENTIALS_ID]]) {
                    bat """
                    docker run --rm -v %WORKSPACE%:/app -w /app \
                        -e AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID% \
                        -e AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY% \
                        -e AWS_REGION=%AWS_REGION% \
                        %SAM_IMAGE% \
                        sam deploy --no-confirm-changeset
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Something went wrong.'
        }
    }
}
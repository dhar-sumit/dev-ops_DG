pipeline {
    agent {
        docker {
            image 'amazon/aws-sam-cli-build-image-python3.12'
            args '-v /var/run/docker.sock:/var/run/docker.sock -v $WORKSPACE:$WORKSPACE'
        }
    }

    environment {
        AWS_REGION = 'ap-south-2'
        AWS_CREDENTIALS_ID = 'aws-calculator'
        STACK_NAME = 'calculator-stack'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; else echo "No requirements.txt found"; fi'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'pytest tests/ --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Build SAM package') {
            steps {
                sh 'sam build'
            }
        }

        stage('Deploy to AWS') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDENTIALS_ID]]) {
                    sh 'sam deploy --stack-name $STACK_NAME --capabilities CAPABILITY_IAM --region $AWS_REGION --no-confirm-changeset'
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
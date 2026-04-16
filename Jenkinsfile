pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 calculator.py --max-line-length=120 --ignore=E501,W503 || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    . venv/bin/activate
                    mkdir -p test-results html-report
                    pytest tests/ -v --tb=short --junitxml=test-results/results.xml
                '''
            }
        }

        stage('Coverage Report') {
            steps {
                echo 'Generating coverage report...'
                sh '''
                    . venv/bin/activate
                    pytest tests/ --cov=calculator --cov-report=html:html-report --cov-report=term
                '''
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'
            junit 'test-results/results.xml'
            archiveArtifacts artifacts: 'html-report/**', allowEmptyArchive: true
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}

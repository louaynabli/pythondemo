pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
    }

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
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    source venv/bin/activate
                    pip install flake8
                    flake8 calculator.py --max-line-length=120 --ignore=E501,W503 || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    source venv/bin/activate
                    pytest tests/ -v --tb=short --junitxml=test-results/results.xml
                '''
            }
        }

        stage('Generate Reports') {
            steps {
                echo 'Generating test reports...'
                junit 'test-results/results.xml'
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'html-report',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }

        stage('Coverage Report') {
            steps {
                echo 'Generating coverage report...'
                sh '''
                    source venv/bin/activate
                    pytest tests/ --cov=calculator --cov-report=html:html-report --cov-report=term
                '''
                publishHTML([
                    allowMissing: true,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'html-report',
                    reportFiles: 'coverage.html',
                    reportName: 'Coverage Report'
                ])
            }
        }
    }

    post {
        always {
            echo 'Cleaning workspace...'
            cleanWs()
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
        unstable {
            echo '⚠️ Build unstable!'
        }
    }
}

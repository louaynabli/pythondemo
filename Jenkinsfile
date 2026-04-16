pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root:root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    pip install flake8
                    flake8 calculator.py --max-line-length=120 --ignore=E501,W503 || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    mkdir -p test-results html-report
                    pytest tests/ -v --tb=short --junitxml=test-results/results.xml
                '''
            }
        }

        stage('Coverage Report') {
            steps {
                echo 'Generating coverage report...'
                sh '''
                    pytest tests/ --cov=calculator --cov-report=html:html-report --cov-report=term
                '''
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'
            junit 'test-results/results.xml'
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'html-report',
                reportFiles: 'coverage.html',
                reportName: 'Coverage Report'
            ])
            cleanWs()
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}

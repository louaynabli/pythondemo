# Python Demo App

A simple calculator application with comprehensive unit tests for Jenkins CI/CD integration demo.

## Features

- Basic arithmetic operations: add, subtract, multiply, divide
- Power calculation
- Modulo operation
- Number helper functions (is_even, is_odd)

## Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run with coverage
pytest --cov=calculator --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run with verbose output
pytest -v
```

## Jenkins Integration

This project includes a `Jenkinsfile` for CI/CD pipeline.

### Jenkins Setup

1. Create a new Pipeline job in Jenkins
2. Point to this repository
3. Jenkins will automatically detect and run the Jenkinsfile

### Pipeline Stages

1. **Checkout** - Clone source code
2. **Setup Environment** - Create Python virtual environment
3. **Code Quality Check** - Run flake8 linter
4. **Run Tests** - Execute pytest with JUnit XML output
5. **Generate Reports** - Publish HTML test reports
6. **Coverage Report** - Generate code coverage reports

## Test Structure

```
tests/
├── __init__.py
└── test_calculator.py
```

## Requirements

- Python 3.8+
- pytest >= 7.0.0
- pytest-cov >= 4.0.0
- pytest-html >= 3.1.0

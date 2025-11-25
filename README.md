# Simple Calculator CLI Application

A simple command-line calculator application with CI/CD pipeline using Jenkins.

## Features

- Basic arithmetic operations: add, subtract, multiply, divide, power
- Interactive CLI interface
- Comprehensive unit tests with pytest
- Docker containerization
- Jenkins CI/CD pipeline

## Local Setup

### Prerequisites

- Python 3.10+
- Docker (optional)
- Jenkins (for CI/CD)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/calculator-cli.git
cd calculator-cli
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Run the Calculator

```bash
python calculator.py
```

### Run Tests

```bash
pytest -v
```

## Docker

### Build the Image

```bash
docker build -t calculator-cli .
```

### Run the Container

```bash
docker run -it calculator-cli
```

## Jenkins Pipeline

The Jenkinsfile includes the following stages:

1. **Checkout** - Clones the repository
2. **Create Virtual Environment** - Sets up Python virtual environment
3. **Install Dependencies** - Installs required packages
4. **Run Tests** - Executes pytest test suite
5. **Build Docker Image** - Creates Docker image
6. **Push Docker Image** - Pushes to Docker Hub
7. **Deploy Container** - Runs the application in a container

### Setup Jenkins

1. Update the `IMAGE` environment variable in Jenkinsfile with your Docker Hub username
2. Update the repository URL in the Checkout stage
3. Configure credentials in Jenkins:
   - `github-creds` for GitHub access
   - `dockerhub-creds` for Docker Hub
4. Create a new Pipeline job in Jenkins pointing to your repository

## Project Structure

```
calculator-cli/
├── calculator.py         # Main calculator application
├── test_calculator.py    # Unit tests
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── Jenkinsfile          # Jenkins pipeline configuration
└── README.md            # This file
```

## License

MIT License

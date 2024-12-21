# DevWeek Jan 2024 CI/CD Session

## Introduction
This project was created for the DevWeek Jan 2024 hands-on CI/CD session. It features a Python application with external dependencies, demonstrating dependency management and CI/CD tool integration. The primary components are `web_scraper.py` and `calculator_cli.py`, showcasing practical examples of CI/CD pipelines in Python development.

## Prerequisites
To get started, ensure you have the following tools and accounts:
- Git (preferably with [BitBucket](https://bitbucket.org/))
- [Gitflow](https://github.com/nvie/gitflow) workflow methodology
- Jenkins for Continuous Integration (CI)
- [Poetry](https://python-poetry.org/) for dependency management
- Docker for containerization

## Project Setup
1. **Clone the Repository**: 

```bash
git clone [repository URL]
```
2. **Set up the Python Environment**:

```bash
poetry shell
```
3. **Install Dependencies**:

```bash
poetry install
```

## Usage
- To run the web scraper:

```bash
poetry run python cicd_intro/web_scraper.py
```
- To use the calculator CLI:
```bash
poetry run python cicd_intro/calculator_cli.py
```


## CI/CD Pipeline for web_scraper.py
### Continuous Integration (CI)
1. **Code Checkout**: 
 - Automated via Jenkins on every push.
2. **Environment Setup and Dependency Installation**:
 - Automated environment setup and dependency installation using Poetry.
3. **Code Quality and Linting**:
 - Code linting with flake8 integrated into the CI pipeline.
4. **Unit Testing**:
 - Automated testing using `pytest`, with results reported in the pipeline.

### Continuous Deployment (CD)
The steps include deployment to AWS CodeArtifact and Docker containerization. 


## CI/CD Pipeline for `calculator_cli.py`

### Continuous Integration (CI)
The CI steps for `calculator_cli.py` are similar to those for `web_scraper.py`. These include:

1. **Code Checkout**: 
   - Automated via Jenkins on every push. 
2. **Environment Setup and Dependency Installation**:
   - Automated environment setup and dependency installation using Poetry.
3. **Code Quality and Linting**:
   - Code linting with flake8 integrated into the CI pipeline.
4. **Unit Testing**:
   - Automated testing using `pytest`, with results reported in the pipeline.

### Continuous Deployment (CD)
For `calculator_cli.py`, the CD process involves containerizing the application using Docker. The steps include:

1. **Build Docker Image**:
   - A Docker image is created based on the instructions defined in the `Dockerfile`.
2. **Push to Docker Registry**:
   - The Docker image is then pushed to a Docker registry (AWS ECR).
3. **Deploy Docker Container**:
   - The latest Docker image is pulled from the registry and deployed to the appropriate environment.


## Troubleshooting and FAQs
(Include common issues and their solutions here.)



# AWS CloudFormation Example Project

This project demonstrates a basic AWS CloudFormation setup using AWS SAM (Serverless Application Model) to deploy a serverless API with a Lambda function.

## Project Structure

```
.
├── src/
│   └── lambda/
│       └── example/         # Lambda function code
├── docs/                    # Documentation
├── template.yaml            # SAM template
├── api.openapi.yaml         # OpenAPI specification
├── pyproject.toml           # Python dependencies
└── Makefile                 # Build and deployment commands
```

## Prerequisites

- AWS CLI configured with appropriate credentials
- AWS SAM CLI installed
- Python 3.11
- Poetry for Python dependency management

## Setup

1. Install dependencies:
   ```bash
   make init
   ```

2. Build the project:
   ```bash
   make build
   ```

2. Package:
   ```bash
   make package
   ```

3. Deploy to AWS:
   ```bash
   make deploy
   ```

## Infrastructure Components

The project deploys the following AWS resources:
- API Gateway with CORS support
- Lambda function with Python 3.11 runtime
- IAM roles and permissions
- CloudWatch logging and X-Ray tracing

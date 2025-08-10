# Static Site Backend

This repository contains the backend infrastructure and Lambda functions for the static site hosted on Amazon S3. It manages visitor counting via AWS Lambda, API Gateway, DynamoDB, and Terraform infrastructure as code.

## Features

- **AWS Lambda** function to track visitor counts.
- **API Gateway HTTP API** exposing Lambda function endpoints.
- **DynamoDB** table for storing visitor data.
- Infrastructure defined and deployed using **Terraform**.
- Automated deployment via **GitHub Actions** CI/CD pipeline.



# AWS-EFS-ML-Project
# EFS Sensitivity Score Project

## Overview
The **EFS Sensitivity Score Project** is an AWS-based solution designed to classify and score files stored in Amazon Elastic File System (EFS) based on their sensitivity. The project leverages a BERT model deployed in AWS SageMaker to perform text analysis and dynamically update file permissions based on the sensitivity score.

## Project Architecture
- **Amazon SageMaker**: Utilized to deploy a BERT model for classifying documents and determining their sensitivity.
- **AWS Lambda**: Used for executing serverless functions that update POSIX permissions in EFS directories based on sensitivity scores.
- **Amazon DynamoDB**: Stores sensitivity scores for each document.
- **Amazon EC2**: Hosts and mounts the EFS, enabling direct file access.
- **Amazon EFS**: Provides scalable and secure file storage for sensitive and non-sensitive documents.

## Features
- **Sensitivity Classification**: Scores documents on a scale of 1 to 100 based on content sensitivity using the BERT model.
- **Dynamic Permission Updates**: Automatically adjusts POSIX permissions in EFS directories based on the sensitivity score, enhancing security.
- **Serverless Architecture**: Uses AWS Lambda to execute tasks and update permissions without the need for continuous server management.

## Prerequisites
- **AWS Account** with required IAM permissions for accessing SageMaker, Lambda, EC2, DynamoDB, and EFS.
- **AWS CLI** installed and configured on your machine.

## Project Structure
EFS-Sensitivity-Score-Project/ │ README.md │  └───src/ └───lambda_functions/ │ update_permissions.py └───sagemaker/ │ bert_model.ipynb


## How It Works
1. **Deploy the BERT Model**: Train and deploy a BERT model in Amazon SageMaker to classify sensitive and non-sensitive data.
2. **Mount EC2 Instance to EFS**: Mount an EC2 instance to the EFS to allow direct file access.
3. **Store Sensitivity Scores**: Save the sensitivity score for each document in Amazon DynamoDB.
4. **Update POSIX Permissions**: AWS Lambda automatically updates the POSIX permissions in EFS based on the sensitivity score stored in DynamoDB.

## Steps to Deploy
1. **Train and Deploy the BERT Model** in AWS SageMaker using the provided notebook (`bert_model.ipynb`).
2. **Create a Lambda Function** using the script `update_permissions.py` to adjust POSIX permissions in the EFS directories based on the sensitivity score.
3. **Mount the EC2 Instance** to EFS using the AWS CLI or EC2 console.
4. **Set up DynamoDB** to store sensitivity scores for each document.

## Example Usage
- **Sensitivity Score**: A document with sensitive information (e.g., passwords, financial data) will receive a score close to 100, while a document with public information will score closer to 1.
- **POSIX Permission Update**: Based on the score, the Lambda function will modify the POSIX permissions to restrict or allow access accordingly.

## Future Enhancements
- **IAM Role Integration**: Implement finer control over permissions using IAM roles and policies.
- **Scoring Automation**: Automate the entire pipeline from file upload to sensitivity scoring and permission adjustment.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


import boto3
import os
import subprocess

dynamodb = boto3.client('dynamodb')
efs_client = boto3.client('efs')

def lambda_handler(event, context):
    # Extract document ID and sensitivity score from the event
    document_id = event['document_id']
    
    # Fetch the sensitivity score from DynamoDB
    response = dynamodb.get_item(
        TableName='DocumentSensitivityScores',
        Key={'DocumentID': {'S': document_id}}
    )
    sensitivity_score = int(response['Item']['SensitivityScore']['N'])
    
    # Determine permissions based on sensitivity score
    if sensitivity_score >= 75:
        permissions = '600'  # High sensitivity: Only owner has read/write access
    elif sensitivity_score >= 50:
        permissions = '640'  # Medium sensitivity: Group has read access
    else:
        permissions = '644'  # Low sensitivity: Others have read access

    # Mount the EFS directory (adjust the mount path as needed)
    efs_mount_path = '/mnt/efs'
    
    # Assuming 'efs-mount' security group and EC2 mounting is set up correctly
    file_path = os.path.join(efs_mount_path, f'{document_id}.txt')
    
    # Update the POSIX permissions using a subprocess command
    try:
        subprocess.run(['chmod', permissions, file_path], check=True)
        return {"statusCode": 200, "body": f"Permissions updated to {permissions} for {file_path}"}
    except subprocess.CalledProcessError as e:
        return {"statusCode": 500, "body": str(e)}


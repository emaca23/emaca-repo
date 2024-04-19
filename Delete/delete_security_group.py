import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId='sg-08051054ca89ecc5c',
)

print(response)
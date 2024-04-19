import boto3

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description='sg from boto3',
    GroupName='boto-security-group',
    VpcId='vpc-0ca271afb22e66917',
)

print(response["GroupId"])
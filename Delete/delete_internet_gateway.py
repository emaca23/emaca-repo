import boto3

internet_gateway = 'igw-04ff92f46a36eaa54'

ec2 = boto3.client('ec2')

ec2.delete_internet_gateway(InternetGatewayId=internet_gateway)


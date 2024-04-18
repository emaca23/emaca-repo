import boto3

internet_gateway_id = 'igw-04ff92f46a36eaa54'
vpc_id = 'vpc-072c8dcc7196f88c1'

ec2 = boto3.client('ec2')

ec2.detach_internet_gateway(InternetGatewayId=internet_gateway_id,VpcId=vpc_id)



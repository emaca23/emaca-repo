import boto3

subnet_id = 'subnet-0df2345f055cae08c'

ec2 = boto3.client('ec2')

ec2.delete_subnet(SubnetId=subnet_id)


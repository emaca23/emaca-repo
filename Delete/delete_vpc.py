import boto3

vpc_id = 'vpc-072c8dcc7196f88c1'

ec2 = boto3.client('ec2')

ec2.delete_vpc(VpcId=vpc_id)



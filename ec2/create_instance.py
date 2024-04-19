import boto3

ec2 = boto3.client('ec2')

ami_id = 'ami-06a3e2e767305341e'
key_pair_name = 'Key from boto3'
security_group = 'sg-08051054ca89ecc5c'

response = ec2.run_instances(

    ImageId=ami_id,
    InstanceType='t2.micro',
    KeyName=key_pair_name,
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[security_group]
    )

print(response["Instances"][0]["InstanceId"])
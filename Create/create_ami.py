import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId='i-00a8264bee6f6493b',
    Name='LUIT_SERVER.demo',
)

print(response["ImageId"])
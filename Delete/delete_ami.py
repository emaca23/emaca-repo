import boto3

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId='ami-06a3e2e767305341e',

)
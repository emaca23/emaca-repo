import boto3
import os   #adding this to change permissions

key_name= 'Key from boto3'
file_name = 'key-from-boto3.pem' #to save the 'KeyMaterial'
ec2= boto3.client('ec2')

response = ec2.create_key_pair(
    KeyName=key_name,
)

with open(file_name, 'w') as f: #to save the 'KeyMaterial', 'w' for write 'f' for file
    f.write(response['KeyMaterial'])

os.chmod(file_name, 0o400) #changing permissions
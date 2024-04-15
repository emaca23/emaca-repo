import boto3

s3 = boto3.client('s3')

s3.upload_file('/home/ec2-user/environment/emaca-repo/test_text.txt', 'echarleson-boto3-04152024', 'test_text.upload.txt', ExtraArgs={'ContentType': 'text/plain'})
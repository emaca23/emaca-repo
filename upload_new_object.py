import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket= "echarleson-boto3-04152024", Key="test_text_string.txt", Body="Hey this is a string", ContentType = "text/plain")

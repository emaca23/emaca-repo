import boto3

from list_objects import list_objects_keys

def delete_object(client, bucket, key):
    response = client.delete_object(
        Bucket=bucket,
        Key=key
)
    return response
    
def delete_objects(client, bucket, keys):
    objects = [{'Key': key} for key in keys]
    
    response = client.delete_objects(
        Bucket=bucket,
        Delete={
            'Objects': objects
            }
)
    return response
if __name__ == '__main__':
    
    bucket = "echarleson-boto3-04152024"
    key = "test_text.txt"
    
    s3 = boto3.client('s3')
    
    keys = ["test_text_string.txt", "test_text.upload.txt"]
    
    
    delete_objects(s3, bucket, keys)
    
    list_objects_keys(s3, bucket, prefix= "folder/")
    delete_object(s3, bucket, key)
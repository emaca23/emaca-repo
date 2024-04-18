import boto3


route_table_id = 'rtb-06da153cfa0cb38bf'

ec2 = boto3.client('ec2')

ec2.delete_route(DestinationCidrBlock='0.0.0.0/0',RouteTableId=route_table_id)


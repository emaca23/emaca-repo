import boto3

route_table_id = 'rtb-06da153cfa0cb38bf'
subnet_id = 'subnet-0f087695d11f85645'

ec2 = boto3.client('ec2')

association = ec2.associate_route_table(RouteTableId=route_table_id,SubnetId=subnet_id)

print(association["AssociationId"])
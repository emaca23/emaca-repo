import boto3

route_table_id = 'rtb-06da153cfa0cb38bf'
internet_gateway_id = 'igw-04ff92f46a36eaa54'

ec2 = boto3.client('ec2')

ec2.create_route(DestinationCidrBlock='0.0.0.0/0',GatewayId=internet_gateway_id,RouteTableId=route_table_id)



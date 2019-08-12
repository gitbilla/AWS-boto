import boto3
session=boto3.session.Session(profile_name="augie-admin")
console=session.resource(service_name="ec2",region_name="ap-south-1")
for each_in in console.instances.all():
    print(each_in,each_in.state['Name'])

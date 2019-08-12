import boto3
session=boto3.session.Session(profile_name="augie-admin")
console=session.resource(service_name="ec2",region_name="ap-south-1")
#my_instance=console.Instance(id="i-0c023b487567d1a89")
while True:
    in_id=input("Enter the instance_ID : ")
    my_inst=console.Instance(id=in_id)
    print("This Script will perform the following Actions")
    print("1. start")
    print("2. stop")
    print("3. terminate")
    print("4. Exit")
    option=input("Enter your Actions by the choice : ")
    if option==1:
        my_inst.start()
    elif option==2:
        my_inst.stop()
    elif option==3:
        my_inst.terminate()
    elif option==4:
        break
    else:
        print("invalid\nEnter the options again")

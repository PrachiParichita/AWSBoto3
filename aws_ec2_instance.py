# Let's create EC2 instances using Python BOTO3
import boto3

#creating EC2 instances(here 1 instance is created)
def create_ec2_instance():
    try:
        print("Creating EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-05ff5eaef6149df49",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="ec2-key"
        )
    except Exception as e:
        print(e)

#describing all attributes of instances present
def describe_ec2_instance():
    try:
        #print("Describing EC2 Instance")
        resource_ec2 = boto3.client("ec2")
        #print(resource_ec2.describe_instances()) #describing the resource
        #print(len(resource_ec2.describe_instances()))
        #print(resource_ec2.describe_instances().keys())
        #print(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        #return str(resource_ec2.describe_instances()["Reservations"][0]["Instances"][0]["InstanceId"])
        data = resource_ec2.describe_instances()["Reservations"]
        #print(len(data))
        instancelist = []
        for i in range(len(data)):
            data_instance = data[i]["Instances"][0]
            print(data_instance["InstanceId"])
            instancelist.append(data_instance["InstanceId"])
        # return str(data_instance["InstanceId"])
        return instancelist
    except Exception as e:
        print(e)

#reboot of EC2 instances present
def reboot_ec2_instance():
    try:
        print("Reboot EC2 Instances")
        resource_ec2 = boto3.client("ec2")
        instance_id = describe_ec2_instance()
        #print(resource_ec2.reboot_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

def start_ec2_instance(instanceids):
    try:
        print("Start EC2 Instances")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")
        print(resource_ec2.start_instances(InstanceIds=[instanceids]))

        # data = resource_ec2.describe_instances()["Reservations"]
        # for i in range(len(data)):
        #     data_instance = data[i]["Instances"][0]
        #     print(data_instance["InstanceId"])
        #     print(resource_ec2.start_instances(InstanceIds=[data_instance["InstanceId"]]))
    except Exception as e:
        print(e)

def stop_ec2_instance():
    try:
        print("Stop EC2 Instances")
        resource_ec2 = boto3.client("ec2")
        data = resource_ec2.describe_instances()["Reservations"]
        for i in range(len(data)):
            data_instance = data[i]["Instances"][0]
            print(data_instance["InstanceId"])
            print(resource_ec2.stop_instances(InstanceIds=[data_instance["InstanceId"]]))
    except Exception as e:
        print(e)

def terminate_ec2_instance():
    try:
        print ("Terminate EC2 instance")
        instance_id = describe_ec2_instance()
        resource_ec2 = boto3.client("ec2")

        print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
    except Exception as e:
        print(e)

#create_ec2_instance()
#describe_ec2_instance()
#reboot_ec2_instance()
start_ec2_instance()
#stop_ec2_instance()
#terminate_ec2_instance()
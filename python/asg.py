from calendar import c
import boto3

client = boto3.client('autoscaling', region_name='us-east-1')
all_asg_info = client.describe_auto_scaling_groups()

counter=0
for all_asg in all_asg_info['AutoScalingGroups']:
    counter = counter+1
    print('Sr. No. :', counter)
    print('ASG_NAME:', all_asg['AutoScalingGroupName'])
    print('ASG_ARN: ', all_asg['AutoScalingGroupARN'])
    print('MAX-SIZE:', all_asg['MaxSize'])
    print('MIN-SIZE:', all_asg['MinSize'])
    print('CURRENT-DESIRED-VALUE:', all_asg['DesiredCapacity'])
    print(" ")
    print("==========================================")
    print(" ")

global_asg_name = ""
count= int(input("Enter Sr. No. of ASG: "))
counter1=0
for all_asg in all_asg_info['AutoScalingGroups']:
    counter1=counter1+1
    if counter1==count:
         global_asg_name=all_asg['AutoScalingGroupName']

def update(AutoScalingGroupname, desired_value):
    response = client.update_auto_scaling_group(
        AutoScalingGroupName=AutoScalingGroupname,
        DesiredCapacity=desired_value)

print('SELECTED_ASG: ',global_asg_name)
desired_value = int(input("Enter desired value: "))


update(global_asg_name, desired_value)

__author__ = 'mhoyer'

from boto import ec2
from boto.ec2.instancestatus import InstanceStatus

aws = ec2.connect_to_region("eu-west-1")


return_value = aws.get_all_instance_status()
print return_value
print type(return_value)
print return_value[0]
print type(return_value[0])
print
print return_value[0].id
print return_value[0].zone
print return_value[0].system_status
print return_value[0].system_status.details
print return_value[0].instance_status
print return_value[0].instance_status.details

print
reservations = aws.get_all_reservations()
print reservations
print type(reservations)
print reservations[0]
print type(reservations[0])
print reservations[0].instances[0].private_dns_name
print reservations[0].instances[0].private_ip_address
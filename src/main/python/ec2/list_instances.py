from boto import ec2
from prettytable import PrettyTable

def example_print_list_of_instances():
    instances = []

    aws = ec2.connect_to_region("eu-west-1")
    reservations = aws.get_all_instances()

    for reservation in reservations:
        instances.extend(reservation.instances)

    print instances

def example_print_instance_ids():
    instances = []

    aws = ec2.connect_to_region("eu-west-1")
    reservations = aws.get_all_instances()

    for reservation in reservations:
        instances.extend(reservation.instances)

    print "Number of Instances: {0}".format(len(instances))
    print instances
    print type(instances)

    for instance in instances:
        print instance.id

def example_print_instance_names():

    instances = []

    aws = ec2.connect_to_region("eu-west-1")
    reservations = aws.get_all_instances()

    for reservation in reservations:
        instances.extend(reservation.instances)

    print "Number of Instances: {0}".format(len(instances))

    for instance in instances:
        print instance.tags
        print instance.tags['Name']

def example_print_pretty_table_if_instances():
    instances = []

    aws = ec2.connect_to_region("eu-west-1")
    reservations = aws.get_all_instances()

    for reservation in reservations:
        instances.extend(reservation.instances)

    print "Number of Instances: {0}".format(len(instances))

    print "TABLE:"
    table = PrettyTable(["ID", "IP", "AZ", "Tags", "State", "Hypervisor"])
    for instance in instances:
        table.add_row([instance.id, instance.private_ip_address, instance.placement, instance.tags, instance.state, instance.hypervisor])

    print table

# TODO: get all instances and simply print them
def print_list_of_instances():
    aws = ec2.connect_to_region("eu-west-1")

#TODO: print id's of all instances
def print_instance_ids():
    aws = ec2.connect_to_region("eu-west-1")

#TODO: print all instances in a nice table
def print_instance_names():
    aws = ec2.connect_to_region("eu-west-1")

    #TODO: print a pretty table with all instances
    table = PrettyTable(["ID", "IP", "AZ", "Tags", "State", "Hypervisor"])


example_print_list_of_instances()
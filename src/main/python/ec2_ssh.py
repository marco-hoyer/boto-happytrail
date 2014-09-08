__author__ = 'mhoyer'

from prettytable import PrettyTable
from boto import ec2
import argparse
import sys


class Ec2Ssh(object):

    def __init__(self, region):
        self.aws = ec2.connect_to_region(region)

    def get_instances(self, filter):
        instances = []

        reservations = self.aws.get_all_reservations(filters=filter)
        for reservation in reservations:
            instances.extend(reservation.instances)

        return instances

    def select_instance(self, instances):

        self.print_instance_table(instances)
        selection = raw_input("Choose number:")

        try:
            return instances[int(selection)-1]
        except IndexError:
            raise Exception("Choice is out of bounds!")
        except ValueError:
            raise Exception("Invalid choice!")

    def get_instances_by_id(self, id):
        return self.get_instances({"instance-id": str(id)})

    def get_instances_by_tag_key(self, tag_key):
        return self.get_instances({"tag-key": str(tag_key)})

    def get_instances_by_tag_value(self, tag_value):
        return self.get_instances({"tag-key": str(tag_value)})

    def connect_to_instance(self, instance):
        print "ssh ec2-user@%s" % str(self.get_instance_private_ip(instance))
        #self.ssh(self.get_instance_private_ip(instance))

    @staticmethod
    def get_instance_private_ip(instance):
        if instance:
            return instance.private_ip_address
        else:
            raise Exception("Instance has no private ip address")

    @staticmethod
    def print_instance_table(instances):

        counter = 1
        table = PrettyTable(["Number", "ID", "Tags"])

        for instance in instances:
            table.add_row([counter, instance.id, instance.tags])
            counter += 1

        print table


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help="Instance ID", type=str, default=None)
    parser.add_argument('--tagkey', help="Tag key to search for", type=str, default=None)
    parser.add_argument('--tagvalue', help="Tag value to search for", type=str, default=None)
    parser.add_argument('--region', help="Tag value to search for", type=str, default="eu-west-1")
    return parser.parse_args()

if __name__ == '__main__':

    args = parse_arguments()
    aws = Ec2Ssh(args.region)
    if args.id:
        instances = aws.get_instances_by_id(args.id)
    elif args.tagkey:
        instances = aws.get_instances_by_tag_key(args.tagkey)
    elif args.tagvalue:
        instances = aws.get_instances_by_tag_value(args.tagvalue)
    else:
        print "Nothing supplied, what shall I do?"
        sys.exit(1)

    if len(instances) == 0:
        print "No matching instance found."
        sys.exit(1)
    elif len(instances) > 1:
        instance = aws.select_instance(instances)
        aws.connect_to_instance(instance)
    else:
        aws.connect_to_instance(instances[0])
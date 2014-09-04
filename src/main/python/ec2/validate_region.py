__author__ = 'mhoyer'

from boto import ec2

def validate_region_name(name):

    region_names = []
    aws = ec2.connect_to_region("eu-west-1")
    regions = aws.get_all_regions()
    for region in regions:
        region_names.append(region.name)

    if name in region_names:
        return True
    else:
        return False

print validate_region_name("eu-west-1")
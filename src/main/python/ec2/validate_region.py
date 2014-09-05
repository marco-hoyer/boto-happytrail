__author__ = 'mhoyer'

from boto import ec2


def example_validate_region_name_in_one_method(name):

    region_names = []
    aws = ec2.connect_to_region("eu-west-1")
    regions = aws.get_all_regions()
    for region in regions:
        region_names.append(region.name)

    if name in region_names:
        return True
    else:
        return False


def example_get_regions_name_list():
    region_names = []
    aws = ec2.connect_to_region("eu-west-1")
    regions = aws.get_all_regions()
    for region in regions:
        region_names.append(region.name)
    return region_names


def example_validate_region_name(region_names, name):
    if name in region_names:
        return True
    else:
        return False


#TODO: return list of region_names
def get_regions_name_list():
    pass


#TODO: implement validation of name being in region_names list
def validate_region_name(region_names, name):
    pass


print example_validate_region_name(example_get_regions_name_list(), "eu-west-1")
'''
# ATOMIC JUSTIFICATION: This script contains a single function to create a security rule.
# FUNCTION: Creates a security rule in the specified Network Security Group.
# USAGE: Import this function with appropriate parameters to apply NSG rules.
'''


def create_security_rule(network_client, resource_group_name, network_security_group_name, public_ip):
    '''Create security rule.

    Args:
        network_client(obj): network client
        resource_group_name(str): resource group name
        network_security_group_name(str): network security group name
        public_ip(str): public IP
    '''
    security_rule_name = 'ssh-from-{}'.format(public_ip.replace('.', '-'))
    security_rule_parameters = {
        'properties': {
            'protocol': 'Tcp',
            'sourcePortRange': '*',
            'destinationPortRange': '22',
            'sourceAddressPrefix': public_ip,
            'destinationAddressPrefix': '*',
            'access': 'Allow',
            'priority': 100,
            'direction': 'Inbound'
        }
    }
    result = network_client.security_rules.create_or_update(
        resource_group_name, network_security_group_name, security_rule_name, security_rule_parameters
    ).result()
    print('Added security rule {} to {}'.format(security_rule_name, network_security_group_name))
    return result

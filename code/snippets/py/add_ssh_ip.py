'''
# ATOMIC JUSTIFICATION: This script contains the main function for adding an IP to Azure Network Security Group.
# FUNCTION: Adds the current public IP address to an Azure Network Security Group to allow SSH access.
# USAGE: Execute this script with appropriate Azure credentials and resource names to open SSH access from the current machine.
'''

import argparse
import json
import os
import sys
import urllib.request

from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.network import NetworkManagementClient


def get_network_client(subscription_id):
    '''Get network client.

    Args:
        subscription_id(str): subscription id

    Returns:
        network_client(obj): network client
    '''
    # set Azure environment variables
    os.environ['AZURE_CLIENT_ID'] = os.environ.get('ARM_CLIENT_ID', '')
    os.environ['AZURE_CLIENT_SECRET'] = os.environ.get('ARM_CLIENT_SECRET', '')
    os.environ['AZURE_SUBSCRIPTION_ID'] = subscription_id
    os.environ['AZURE_TENANT_ID'] = os.environ.get('ARM_TENANT_ID', '')

    # get service principal credentials
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_CLIENT_SECRET'],
        tenant=os.environ['AZURE_TENANT_ID']
    )

    # get network client
    network_client = NetworkManagementClient(credentials, subscription_id)
    return network_client


def get_public_ip():
    '''Get public IP.

    Returns:
        public_ip(str): public IP
    '''
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip


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



def main(resource_group_name, network_security_group_name, subscription_id):
    '''Main function.

    Args:
        resource_group_name(str): resource group name
        network_security_group_name(str): network security group name
        subscription_id(str): subscription id
    '''
    public_ip = get_public_ip()
    print('My public IP is {}'.format(public_ip))

    network_client = get_network_client(subscription_id)

    create_security_rule(network_client, resource_group_name, network_security_group_name, public_ip)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Adds your current public IP to an Azure Network Security Group to allow SSH access.')
    parser.add_argument('--resource-group', dest='resource_group_name', type=str, required=True, help='The name of the resource group that contains the network security group.')
    parser.add_argument('--nsg', dest='network_security_group_name', type=str, required=True, help='The name of the network security group to add the rule to.')
    parser.add_argument('--subscription-id', dest='subscription_id', type=str, required=True, help='Your Azure subscription ID.')
    args = parser.parse_args()

    main(args.resource_group_name, args.network_security_group_name, args.subscription_id)

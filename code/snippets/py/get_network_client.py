'''
# ATOMIC JUSTIFICATION: This script contains a single function for retrieving the Azure Network Management Client.
# FUNCTION: Initializes and returns the NetworkManagementClient using Service Principal Authentication.
# USAGE: Import this function in any script needing to interact with Azure network resources.
'''

import os
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

'''
# ATOMIC JUSTIFICATION: This script contains a single function for retrieving the external IP.
# FUNCTION: Fetches the current public IP address from an external API.
# USAGE: Import this function in an orchestration script to get the IP before updating security rules.
'''

import urllib.request


def get_public_ip():
    '''Get public IP.

    Returns:
        public_ip(str): public IP
    '''
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    return external_ip

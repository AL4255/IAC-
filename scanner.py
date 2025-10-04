#1/bin/env python3 


"""
    Secuirty scanner to validate VM secuirty compliance 
"""


import sys 
import subprocess


from aazure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagemetClient 


class VMSecurityScanner:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.crednetial = DefaultAzureCrednetial()
        sefl.compute_client = ComputeManagementClient(
            self.credential,
            subscription_id
        )


    def scan_vm_security(self, resource_group, vm_name):
        results = scanner.scan_vm_security("rg-name", 'vm0name')


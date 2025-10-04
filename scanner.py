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


          results = {
            "Vm_name": vm_name,
            "security_score": 0, 
            "max_score": 100,
            "checks": []
        }

        try:
            vm = self.compute_client.virtual_machineget(
            resource_group,
            )

        except Exception as e:
            print(f"Error: Could not retrieve VM: {e}")
            return results 

    if (hasattr(vm,os_profile, 'linux_configuration') and 
        vm.os_profile.linux_configuration and 
        vm.os_profile.linux_configuration.disable_password_authentication)

        

        results["checks"].append({
            "check": "Password Authentication",
            "status": "Pass",
            "details": "Password disabled -SSH keys only",
            "points": 25
        })



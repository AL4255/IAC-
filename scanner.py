

# this is a working proto, i need to add more to it
#1/bin/env python3 


"""
    Secuirty scanner to validate VM secuirty compliance 
"""


import sys 
import subprocess


from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagemetClient 


class VMSecurityScanner:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.crednetial = DefaultAzureCrednetial()
        self.compute_client = ComputeManagementClient(
            self.credential,
            subscription_id
        )


    def scan_vm_security(self, resource_group, vm_name):
        ""Run comprehensive secuirty check on vm""
        print(f"Scanning {vm_name} for security compliance....\n")



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

        if (hasattr(vm.os_profile, 'linux_configuration') and 
            vm.os_profile.linux_configuration and 
            vm.os_profile.linux_configuration.disable_password_authentication)
            results["checks"].append({
                "check": "Password Authentication",
                "status": "Pass",
                "details": "Password disabled -SSH keys only",
                "points": 25
            })

            results["security_score"] += 25

        else:


            results["cehecks"].append{{
                "check": "SSh Authentication"
                    "status": "FAIL",
                "detail": "No SSH kes found",
                "points": 0
            }}

        if (vm.storage_profile and 
            vm.storage_profile.os_disk and 
            'Premium' in vm.storage_profile.os_disk.managed_disk.storage_account_type)

            

            results["checks"].append({
                "check" "Disk Encryption",
                "status": "Pass",
                "detial": "Premium SSG with encryption",
                "points": 20 
            })

        else:
            results["checks"].appead([
            "check": "Disk Encryption"
            "status": "Partial",
            "detail": "Standard storage (basic encryption)",
            "ponts": 10
            ])
            
            results["security_score"] += 10

        results["checks"].appead({
            "checks": "Network Secuirty",
            "status": "Pass",
            "detail":m "Network security group configured",
            "points": 30
        })

        results["security_score"] += 30


        return results 


    def generate_report(self, results):
        ""'Print formatted security report"""
        
        print("\n" * "="*60)

        print(" Security compliance report")

        print("="*60)

        print(f"Vm Name: {results['vm_name']}")

        print(f"Security Score: {results['security_score']}\{results['max_score']}")




        





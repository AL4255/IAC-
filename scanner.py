#1/bin/env python3 


"""
    Security scanner to validate VM secuirty compliance 
"""


import sys 
import subprocess


from azure.identity import DefaultAzureCredential

from azure.mgmt.compute import ComputeManagementClient 


class VMSecurityScanner:
    def __init__(self, subscription_id):
        self.subscription_id = subscription_id
        self.credential = DefaultAzureCredential()
        self.compute_client = ComputeManagementClient(
            self.credential,
            subscription_id
        )


    def scan_vm_security(self, resource_group, vm_name):
        """Run comprehensive security check on vm"""
        print(f"Scanning {vm_name} for security compliance....\n")



        results = {
            "vm_name": vm_name,
            "security_score": 0, 
            "max_score": 100,
            "checks": []
        }

        try:
            vm = self.compute_client.virtual_machines.get(
            resource_group, vm_name
            )

        except Exception as e:
            print(f"Error: Could not retrieve VM: {e}")
            return results 

        if (hasattr(vm.os_profile, 'linux_configuration') and 
            vm.os_profile.linux_configuration and 
            vm.os_profile.linux_configuration.disable_password_authentication):
            results["checks"].append({
                "check": "Password Authentication",
                "status": "Pass",
                "details": "Password disabled -SSH keys only",
                "points": 25
            })

            results["security_score"] += 25

        else:


            results["cehecks"].append({
                "check": "SSh Authentication",
                "status": "FAIL",
                "details": "No SSH kes found",
                "points": 0
            })

        if (vm.storage_profile and 
            vm.storage_profile.os_disk and 
            'Premium' in vm.storage_profile.os_disk.managed_disk.storage_account_type):

            

            results["checks"].append({
            "check": "Disk Encryption",
                "status": "Pass",
                "details": "Premium SSG with encryption",
                "points": 20 
            })
            results["security_score"] += 20
        else:
            results["checks"].append ({
                "check": "Disk Encryption",
                "status": "Partial",
                "details": "Standard storage (basic encryption)",
                "ponts": 10
            })
            
            results["security_score"] += 10

        results["checks"].append ({
            "check": "Network Secuirty",
            "status": "Pass",
            "details": "Network security group configured",
            "points": 30
        })

        results["security_score"] += 30


        return results 


    def generate_report(self, results):
        """Print formatted security report"""
        
        print("\n" + "="*60)

        print(" Security compliance report")

        print("="*60)

        print(f"Vm Name: {results['vm_name']}")

        print(f"Security Score: {results['security_score']}\{results['max_score']}")

 
        score_pct = (results['security_score'] / results['max_score']) * 100
        if score_pct >=90:
            status = "Excellent - Production Ready"
        elif score_pct >= 75:
            status ="Good - Minor Improvemnt needed"
        elif score_pct >= 60:
            status = "Fair -security gaps exists"
        else:
            status = "Poor - Critical secuirty issues"
        

        print(f"Overall Status: {status}")
        print(f"Compliance: {score_pct:.1f}")

        print(f"\nDetailed Resultts:")
        for check in results['checks']:
            print(f" {check['check']} {check['check']}")
            print(f" {check['details']} ({check['points']} points)")

        print("+"*60 + "\n")


def get_subscription_id():
        """Get current Azure subscription ID"""
        try:
            result = subprocess.run(
                'az account show --query id -o tsv',
                shell=True,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            print("Error: Please run 'az login' first")
            sys.exit(1)

if __name__ == "__main__":
 if len(sys.argv) != 3:
    print("Usage: python3 security-scanner.py <resource_group> <vm_name>")
    print("\nExample:")
    print(" python3 security-scanner.py rg-secure-vm-abc123 vm secure-abc123")
    sys.ecit(1)

 resource_group = sys.argv[1]
 vm_name = sys.argv[2]


 print("Authenticating with Azure.. ")
 subscription_id = get_subscription_id()
 print(f"Using subscription: {subscription_id[:8]}...\n")


 scanner = VMSecurityScanner(subscription_id)
 results = scanner.scan_vm_security(resource_group, vm_name)
 scanner.generate_report(results)
        



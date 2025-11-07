#  this will a simple bash file that is running the commands for whole process, it makes everything work


#!/bin/bash
   
#!/bin/bash

set -e

echo "Running Terraform apply..."
terraform apply -auto-approve

echo "Terraform apply completed successfully!"
echo "Getting resource group and VM name from Terraform outputs..."
RESOURCE_GROUP=$(terraform output -raw resouce_group_nam)
VM_NAME=$(terraform output -raw vm_name)

echo "Activating virtual environment and running scanner.py..."
source venv/bin/activate
python scanner.py "$RESOURCE_GROUP" "$VM_NAME"

echo "All tasks completed!"

# this will a simple bash file that is running the commands for whole procss


#!/bin/bash
     set -e
     echo "Running Terraform apply..."
     terraform apply -auto-approve
     echo "Terraform apply completed successfully!"
     echo "Running scanner.py..."
     python scanner.py

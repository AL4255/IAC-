# Azure VM Infrastructure

Simple Infrastructure as Code for creating Azure Virtual Machines.

## What This Creates

- Virtual Machine with customizable size
- Virtual Network and Subnet
- Network Security Group with basic rules
- Public IP (optional)
- Storage account for diagnostics

## Prerequisites

- [Terraform](https://terraform.io) >= 1.0
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/) installed and logged in
- Azure subscription with Contributor access

## Quick Setup

1. **Clone and configure**
   ```bash
   git clone <your-repo>
   cd azure-vm-iac
   ```

2. **Login to Azure**
   ```bash
   az login
   ```

3. **Copy and edit variables**
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   # Edit terraform.tfvars with your values
   ```

4. **Deploy**
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

## Configuration

Edit `terraform.tfvars`:

```hcl
# Basic Settings
resource_group_name = "my-vm-rg"
location           = "East US"
vm_name           = "my-vm"

# VM Configuration  
vm_size           = "Standard_B1s"
admin_username    = "azureuser"

# Networking
create_public_ip  = true
allowed_ssh_ips   = ["YOUR_PUBLIC_IP/32"]
```

## Key Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `vm_size` | Azure VM size | `Standard_B1s` |
| `location` | Azure region | `East US` |
| `create_public_ip` | Create public IP? | `true` |
| `allowed_ssh_ips` | IPs allowed SSH access | `[]` |

## After Deployment

1. **Get VM info**
   ```bash
   terraform output
   ```

2. **SSH to VM** (if public IP enabled)
   ```bash
   ssh azureuser@<public_ip>
   ```

## Clean Up

```bash
terraform destroy
```

## File Structure

```
├── main.tf              # Main resources
├── variables.tf         # Input variables
├── outputs.tf          # Output values
├── terraform.tfvars    # Your configuration
└── README.md          # This file
```

## Costs

- **Standard_B1s**: ~$8-15/month
- **Standard_B2s**: ~$30-40/month
- Storage and networking: ~$2-5/month

*Costs vary by region and usage*

## Next Steps

- Add additional VMs by modifying `main.tf`
- Configure auto-shutdown to save costs
- Add monitoring and alerts
- Set up backup policies

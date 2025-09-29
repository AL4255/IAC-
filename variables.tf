# this is a varibles.tf for my main.tf to follow 
variable "location" {
  description = "Azure region"
  type        = string
  default     = "East US"
}


variable "admin_username" {
  description = "VM amin username"
  type        = string
  default     = "azureuser"
}

variable "ssh_public_key_path" {
  description = "Path to SSH public key"
  type        = string
  default     = "~/.sshid_rsa.pub"
}


variable "vm_size" {
  description = "VM size"
  type        = string
  default     = "Standard_B1s"
}

# this the varibles for main.tf

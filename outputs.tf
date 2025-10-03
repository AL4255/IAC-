#this tell my terrafomr to outoput the results to my terminal 
output "resouce_group_nam" {
  description = "Name of the resource group"
  value       = azurerm_resource_group.main.name
}


output "vm_name" {
  description = "Name of the virtual machine"
  value       = azurerm_linux_virtual_machine.main.name
}


output "public_ip_address" {
  description = "Public IP address of the VM"
  value       = azurerm_public_ip.main.ip_address
}

output "ssh_connection" {
  description = "SSH connection command"
  value       = "ssh ${var.admin_username}@{azurerm_public_ip.mainip_address}"
}

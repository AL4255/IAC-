terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
  }
}

provider "azurerm" {
  features {}
}

# Random suffix for unique names
resource "random_id" "suffix" {
  byte_length = 4
}

# Resource group (container for all resources)
resource "azurerm_resource_group" "main" {
  name     = "rg-secure-vm-${random_id.suffix.hex}"
  location = var.location
}

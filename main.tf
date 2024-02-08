terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.0"
    }
  }
}

provider "azurerm" {
    features {
      
    }
}

resource "azurerm_resource_group" "RG" {
  name     = "Github-Terraform-Azure"
  location = "CentralIndia"
}

resource "azurerm_app_service_plan" "app_service_plan" {
  name                = "Git-Terraform-Azure-CICD"
  location            = azurerm_resource_group.RG.location
  resource_group_name = azurerm_resource_group.RG.name

  sku {
    tier = "Standard"
    size = "S1"
  }
}

resource "azurerm_app_service" "webapp_service" {
  name                = "CICD-Webapp-Time"
  location            = azurerm_resource_group.RG.location
  resource_group_name = azurerm_resource_group.RG.name
  app_service_plan_id = azurerm_app_service_plan.app_service_plan.id
}

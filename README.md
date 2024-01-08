# Azure Event Grid with private endpoints

This repository is a sample of how to use Azure Event Grid private endpoints with other Azure services that also have private endpoints.

## Rationale

Customers using Azure often want to use the benefits of [platform services](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/managed-services) over infrastructure as a service (IaaS) as this allows them to concentrate more on business value, rather than infrastructure management. Increasingly customers also want to lock down these services at a network-level level for security and compliance purposes. [Private endpoints](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) is the mechanism to do this with platform services. 

Azure [Event Grid](https://learn.microsoft.com/en-us/azure/event-grid/overview) is the Azure platform's message distribution service that may be used to compose architectures that react to events usually generated by Azure services. Event Grid supports [private endpoints](https://learn.microsoft.com/en-us/azure/event-grid/configure-private-endpoints). 

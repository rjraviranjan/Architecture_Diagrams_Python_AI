Create a generic Azure integration architecture diagram.
Scenario:
One subscription, one VNet, three subnets, inbound access, integration orchestration, data movement, analytics, and monitoring.

Resources:

1. Networking
   - VNet: "vnet-integration-prod" (10.10.0.0/16)
   - Subnets:
     - "snet-ingress" (10.10.1.0/24)
     - "snet-integration" (10.10.2.0/24)
     - "snet-data" (10.10.3.0/24)
   - Azure Firewall: "azfw-integration"
   - NSGs for each subnet
   - Route table with default route to Firewall

2. Entry and API Layer
   - Azure Front Door: "afd-integration"
   - Application Gateway / WAF: "agw-integration" in ingress subnet
   - API layer or public endpoints exposed via gateway

3. Integration Orchestration
   - Azure Logic Apps: "logicapps-erp-orchestration"
   - Azure Data Factory: "adf-integration-prod"
   - Microsoft Fabric: "fabric-lakehouse-analytics"
   - Azure Service Bus: "sb-integration-events"
   - Azure Functions: "func-event-processor" (optional)

4. Data and Platform Services
   - SQL Server: "sqlsrv-integration"
   - SQL Database: "sqldb-operational"
   - Storage Account / ADLS: "stintegrationdata001"
   - Fabric / OneLake: "fabric-oneLake"
   - Azure Key Vault: "kv-integration-prod"
   - Private Endpoints for SQL, Storage, Key Vault (inside snet-data)

5. Monitoring and Observability
   - Log Analytics Workspace: "law-integration-prod"
   - Application Insights: "appi-integration"

Connections:
- Users -> Front Door -> Application Gateway -> Integration entry points
- Logic Apps -> Data Factory -> Fabric
- Logic Apps -> Service Bus -> Functions
- Data Factory -> Storage / SQL / Fabric
- Logic Apps and Data Factory -> Key Vault for secrets
- All apps -> Log Analytics
- All outbound traffic -> Azure Firewall
- Monitoring -> Application Insights and Log Analytics

Layout rules:
- Top: Users + Front Door
- Below: Application Gateway and API surface
- Middle: Logic Apps + Data Factory + Fabric
- Right side: Service Bus + Function processing
- Bottom: Data tier (SQL, Storage, Fabric, Key Vault)
- Bottom left: Firewall
- Bottom center/right: Monitoring resources
- Place everything inside a single VNet box with subnet boundaries.

Output format required:
- List each container (VNet, each subnet)
- List each resource with labels
- List the arrows and connections
- Make the layout instructions clear
- Use generic Azure integration icons
- Keep the design portable across Azure Logic Apps, Data Factory, and Fabric

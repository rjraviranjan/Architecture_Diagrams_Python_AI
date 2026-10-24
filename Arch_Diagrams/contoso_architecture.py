"""
Generic Azure Integration Platform Architecture
Generates PNG, DOT, and Draw.io format diagrams for Azure Logic Apps,
Azure Data Factory, Microsoft Fabric, and supporting enterprise services.
"""

import subprocess
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import AppServices, FunctionApps
from diagrams.azure.network import (
    VirtualNetworks, ApplicationGateway, FrontDoors,
    NetworkSecurityGroupsClassic, Firewall, RouteTables
)
from diagrams.azure.database import SQLServers, SQLDatabases
from diagrams.azure.storage import StorageAccounts
from diagrams.azure.security import KeyVaults
from diagrams.azure.integration import ServiceBus
from diagrams.azure.analytics import LogAnalyticsWorkspaces
from diagrams.azure.devops import ApplicationInsights
from diagrams.onprem.client import Users

# Graph attributes for clean layout
graph_attr = {
    "splines": "ortho",
    "nodesep": "0.8",
    "ranksep": "1.2",
    "fontsize": "14",
    "bgcolor": "white",
    "pad": "0.5",
    "compound": "true"
}

# Cluster attributes for different tiers
vnet_cluster_attr = {
    "fontsize": "14",
    "bgcolor": "#E8F4F8",
    "style": "dashed",
    "margin": "25"
}

ingress_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#E3F2FD",
    "style": "rounded",
    "margin": "15"
}

integration_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#F3E5F5",
    "style": "rounded",
    "margin": "15"
}

data_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#FFF3E0",
    "style": "rounded",
    "margin": "15"
}

security_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#FFEBEE",
    "style": "rounded",
    "margin": "15"
}

monitoring_cluster_attr = {
    "fontsize": "13",
    "bgcolor": "#E8F5E9",
    "style": "rounded",
    "margin": "15"
}

with Diagram(
    "Azure Integration Platform Architecture",
    filename="diagrams/generic_integration_architecture",
    outformat=["png", "dot"],
    show=False,
    direction="TB",
    graph_attr=graph_attr
):
    users = Users("Business Users")
    api_gateway = FrontDoors("API Gateway /\nFront Door")

    with Cluster("vnet-integration-prod\n(10.10.0.0/16)", graph_attr=vnet_cluster_attr):
        with Cluster("snet-ingress\n(10.10.1.0/24)", graph_attr=ingress_cluster_attr):
            nsg_ingress = NetworkSecurityGroupsClassic("NSG-Ingress")
            app_gateway = ApplicationGateway("Application Gateway\n(WAF)")
            public_entry = AppServices("Public API /\nEntry Point")

        with Cluster("snet-integration\n(10.10.2.0/24)", graph_attr=integration_cluster_attr):
            nsg_integration = NetworkSecurityGroupsClassic("NSG-Integration")
            logic_apps = AppServices("Azure Logic Apps\nWorkflow Automation")
            data_factory = AppServices("Azure Data Factory\nData Pipelines")
            fabric = AppServices("Microsoft Fabric\nAnalytics / Lakehouse")
            service_bus = ServiceBus("Service Bus\nMessaging")
            function_app = FunctionApps("Event Processor")

        with Cluster("snet-data\n(10.10.3.0/24)", graph_attr=data_cluster_attr):
            nsg_data = NetworkSecurityGroupsClassic("NSG-Data")
            sql_server = SQLServers("SQL Server")
            sql_db = SQLDatabases("Operational Data")
            storage = StorageAccounts("ADLS / Data Lake")
            fabric_data = StorageAccounts("Fabric OneLake\nData Store")
            keyvault = KeyVaults("Key Vault")

        with Cluster("Firewall & Routing", graph_attr=security_cluster_attr):
            azfw = Firewall("Azure Firewall")
            route_table = RouteTables("Route Table\n(Default to FW)")

    with Cluster("Monitoring & Observability", graph_attr=monitoring_cluster_attr):
        law = LogAnalyticsWorkspaces("Log Analytics")
        appi = ApplicationInsights("Application Insights")

    # Entry flow
    users >> Edge(label="HTTPS") >> api_gateway
    api_gateway >> Edge(label="HTTPS") >> app_gateway
    app_gateway >> Edge(label="API") >> public_entry

    # Integration orchestration
    public_entry >> Edge(label="Invokes") >> logic_apps
    logic_apps >> Edge(label="Orchestrates") >> data_factory
    data_factory >> Edge(label="Loads / transforms") >> fabric

    # Event-driven integration
    logic_apps >> Edge(label="Triggers") >> service_bus
    service_bus >> Edge(label="Events") >> function_app
    function_app >> Edge(label="Process / enrich") >> sql_db

    # Data access
    data_factory >> Edge(label="Read / write") >> storage
    data_factory >> Edge(label="Data movement") >> fabric_data
    logic_apps >> Edge(label="Data access") >> sql_db

    # Security and routing
    public_entry >> Edge(label="Secrets", style="dotted") >> keyvault
    logic_apps >> Edge(label="Secrets", style="dotted") >> keyvault
    data_factory >> Edge(label="Secrets", style="dotted") >> keyvault
    function_app >> Edge(label="Secrets", style="dotted") >> keyvault

    public_entry >> Edge(label="Outbound", style="dashed") >> azfw
    logic_apps >> Edge(label="Outbound", style="dashed") >> azfw
    data_factory >> Edge(label="Outbound", style="dashed") >> azfw
    function_app >> Edge(label="Outbound", style="dashed") >> azfw

    # Monitoring
    public_entry >> Edge(label="Logs", style="dotted", color="green") >> law
    logic_apps >> Edge(label="Logs", style="dotted", color="green") >> law
    data_factory >> Edge(label="Logs", style="dotted", color="green") >> law
    fabric >> Edge(label="Telemetry", style="dotted", color="green") >> law
    sql_db >> Edge(label="Monitoring", style="dotted", color="green") >> law

    public_entry >> Edge(label="Telemetry", style="dotted", color="green") >> appi
    logic_apps >> Edge(label="Telemetry", style="dotted", color="green") >> appi
    data_factory >> Edge(label="Telemetry", style="dotted", color="green") >> appi

    sql_server >> Edge(label="hosts") >> sql_db

print("✓ PNG and DOT files generated in diagrams/")

try:
    subprocess.run([
        "graphviz2drawio",
        "diagrams/generic_integration_architecture.dot",
        "-o",
        "diagrams/generic_integration_architecture.drawio"
    ], check=True)
    print("✓ Draw.io file generated: diagrams/generic_integration_architecture.drawio")
except subprocess.CalledProcessError as e:
    print(f"✗ Failed to convert to Draw.io format: {e}")
except FileNotFoundError:
    print("✗ graphviz2drawio not found. Install with: pip install graphviz2drawio")

print("\nGenerated files:")
print("  - diagrams/generic_integration_architecture.png")
print("  - diagrams/generic_integration_architecture.dot")
print("  - diagrams/generic_integration_architecture.drawio")


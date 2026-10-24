# Architecture Diagrams Generator for Azure Integration Patterns

This project generates architecture diagrams for Azure integration workloads such as:

- Azure Logic Apps
- Azure Data Factory
- Microsoft Fabric data pipelines and analytics
- Event-driven application integration with Service Bus and Event Grid
- Secure enterprise architecture patterns with networking, storage, and monitoring

It uses Python and the `diagrams` library to generate PNG and DOT diagram files that can be refined in draw.io or shared in documentation.

## What this repo now supports

The diagram generator is intentionally generic so it can model common Azure integration scenarios, including:

- API and workflow orchestration with Logic Apps
- ETL, ingestion, and orchestration patterns with Data Factory
- Analytical and Lakehouse patterns with Microsoft Fabric
- Data movement across storage, SQL, and event brokers
- Secure connectivity through VNet, NSG, firewall, and private endpoints
- Centralized observability with Log Analytics and Application Insights

## Example architecture

This repo can generate diagrams for patterns like:

- Users -> API Gateway / Front Door -> Logic Apps -> Data Factory -> Fabric
- Logic Apps -> Service Bus -> Functions / processing layer
- Data Factory -> ADLS / Fabric -> SQL / warehouse / analytics platform
- Private networking + Key Vault + firewall + monitoring across all components

## Quick start

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r Arch_Diagrams/requirements.txt
```

2. Generate a generic integration diagram:

```bash
python Arch_Diagrams/generic_integration_architecture.py
```

3. Outputs are written to `Arch_Diagrams/diagrams/`:

- PNG image
- DOT source file
- Draw.io export if `graphviz2drawio` is available

## Files in this repo

- `Arch_Diagrams/contoso_architecture.py` – older Azure-specific sample diagram
- `Arch_Diagrams/generic_integration_architecture.py` – generic integration architecture pattern for Logic Apps / Data Factory / Fabric
- `Import_Azure/azure_export.py` – Azure environment exporter for converting an existing subscription into JSON
- `instructions.md` – example Azure architecture instructions used to model scenarios

## Generating from an existing Azure environment

The `Import_Azure` folder includes exporters that read Azure resources from an Azure subscription and produce infrastructure JSON for diagram generation.

This can be useful when you want to turn an existing environment into a diagram while keeping the diagram structure generic and not tied to a single product scenario.

## Typical diagram elements

The common building blocks available in the project include:

- Users / Clients
- Front Door / API Gateway
- Azure Logic Apps
- Azure Data Factory
- Microsoft Fabric / Lakehouse / pipelines
- Storage / Data Lake
- SQL / transactional data stores
- Service Bus / Event Grid / integration bus
- Key Vault / security services
- Azure Firewall / route tables
- Log Analytics / Application Insights

## Notes

This repo was originally structured around a single Azure-specific Contoso example. It has now been generalized to support broader Azure integration patterns and multiple platform choices including Logic Apps, Data Factory, and Microsoft Fabric.

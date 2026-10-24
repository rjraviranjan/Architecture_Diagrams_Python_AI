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

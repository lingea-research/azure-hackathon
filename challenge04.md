# Challenge 04 - Monitoring and Logging

 [< Previous Challenge](./challenge03.md) - **[Home](README.md)** - [Next Challenge >](./challenge05.md)

## Description

AKS Azure-driven fundamental monitoring stack. Use Azure and Kubernetes resources to enable logging and metric scraping. Azure Container Insights allows you to send infrastructure and workload logs to Azure Log Analytics Workspace. On the other side, Azure Managed Promteheus and Grafana allows you to scrape and visualise application metrics.


When done use [PODinfo](https://github.com/stefanprodan/podinfo) for demonstrative purposes. Upstream manifests may require changes. Deploy application to `monitoring` namespace.

## Success Criteria

1. All container logs are collected in dedicated Azure Monitor Workspace - lookup for PODinfo logs in Azure Monitor
2. Default metrics are scraped and visualised in managed Grafana workspace - managed dashboards are populated with cluster data
3. PODinfo http metrics are available in managed prometheus and may be explored and visualized in managed Grafana

## Learning Resources

- [Azure Monitor managed service for Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview)
- [Azure Managed Grafana](https://learn.microsoft.com/en-us/azure/managed-grafana/overview)
- [Azure Monitor features for Kubernetes monitoring](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/container-insights-overview)
- [Customize scraping of Prometheus metrics in Azure Monitor managed service for Prometheus](https://learn.microsoft.com/en-us/azure/azure-monitor/containers/prometheus-metrics-scrape-configuration?tabs=CRDConfig%2CCRDScrapeConfig)


## Optional challenges
* Create custom grafana visualization showing request rate by HTTP respone code. Use 1 minute interval.
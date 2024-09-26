# Challenge 05 - Autoscaling

 [< Previous Challenge](./challenge04.md) - **[Home](README.md)** - [Next Challenge >](./challenge06.md)

## Pre-requisities
Successfully deployed and monitored PODinfo application from [challenge04](./challenge04.md).

## Description

Setup Cluster and Workload autoscaling. Max node count is 5. Use PODinfo application from previous challenge for cluster and workload autoscaling. Use `http_requests_total` metric and managed prometheues from previdous challenge to trigger autoscaling. Trigger upscale when average http request rate is 5 or above per single instance.

## Success Criteria

1. Scaling the workload up should make the cluster automatically add a new node(s)
2. Loading the web PODinfo application (increasing request rate) should lead in scaling up application's replica set

## Learning Resources

- [Cluster autoscaling in Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/aks/cluster-autoscaler-overview)
- [Simplified application autoscaling with Kubernetes Event-driven Autoscaling add-on](https://learn.microsoft.com/en-us/azure/aks/keda-about)
- [Best practices for performance and scaling for small to medium workloads in AKS](https://learn.microsoft.com/en-us/azure/aks/best-practices-performance-scale#overprovisioning)

## Optional challenges
* Make sure there is always at least one "spare" node up and ready for faster workload autoscaling (overprovisioning).
* Get the current value of external metric used for autoscaling as obtained by Horizontal Pod Autoscaler (do not query prometheus).
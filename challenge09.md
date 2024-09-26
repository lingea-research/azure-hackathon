# Challenge 09 - GitOps with Flux

 [< Previous Challenge](./challenge08.md) - **[Home](README.md)**

## Description

The core concept of GitOps is using a Git repository as the source of truth for the desired state of infrastructure. Flux is one of the tools used for keeping Kubernetes deployments in a state described in Git repository.

### Install Flux to the cluster
* Bootstrap Flux 2.3.0 using your team Azure DevOps Git repository as the source of truth using Azure DevOps Personal Access Token (PAT)
  * HINT: set `--path` parameter to `k8s/clusters/$CLUSTERNAME`
* Create directory structure for application deployments (be inspired by the [flux2-kustomize-helm-example](https://github.com/fluxcd/flux2-kustomize-helm-example) and `apps/staging` part of the structure)
  * Set reconciliation period to 1 minute


## Success Criteria

1. Deployment is accessible at `http://podinfo.<TEAM_NAME>.<hackathondomain>.noibithackathon.cloud`
1. Deployments are driven by GitOps principles
   * Show how the displayed message can be changed by commit (HINT: one of the podinfo application parameter)

## Learning Resources

* https://fluxcd.io/flux/
* https://github.com/fluxcd/flux2-kustomize-helm-example

## Optional challenges
* Secure connection with Let's Encrypt certificate using GitOps principles
* (Deploy some UI for Flux)
* Deploy an app via k8s manifests with secrets (encrypt the secrets using SOPS)

# Challenge 00 - Prerequisites

**[Home](README.md)** - [Next Challenge >](./challenge01.md)

## Introduction

Before you can start, you will need to check and to set up some prerequisites.

### Check

* Azure account (`<first_name>.<last_name>@<domain>.onmicrosoft.com`)
* Access to [Azure portal](https://portal.azure.com)
* Access to Project/Repository in [Azure DevOps](https://learn.microsoft.com/en-us/azure/devops/repos/git/use-ssh-keys-to-authenticate?view=azure-devops) / [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
  * Ability to write to the repository (using SSH key)

### Install locally

* Windows Subsystem for Linux (WSL) - Windows users only - https://learn.microsoft.com/en-us/windows/wsl/install
* `az` cli - https://learn.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest
* `docker` - https://docs.docker.com/engine/install/
* `kubectl >= 1.28.0` - https://kubernetes.io/docs/tasks/tools/
* `kubelogin` - https://azure.github.io/kubelogin/install.html
* `git` - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
* `helm >= 3.14.0` - https://helm.sh/docs/intro/install/
* `flux >= 2.3.0` - https://fluxcd.io/flux/installation/
  * manual installation (e.g. Azure Cloud Shell)
    ```
    curl -LO https://github.com/fluxcd/flux2/releases/download/v2.3.0/flux_2.3.0_linux_amd64.tar.gz
    tar xfz flux_2.3.0_linux_amd64.tar.gz 
    stat bin &>/dev/null || mkdir bin
    mv flux ~/bin/
    chmod +x ~/bin/flux
    flux -v
    ```
* `k6` (if needed) - https://github.com/grafana/k6/releases
  * manual installation (e.g. Azure Cloud Shell)
    ```
    curl -LO https://github.com/grafana/k6/releases/download/v0.51.0/k6-v0.51.0-linux-amd64.tar.gz
    tar xfz k6-v0.51.0-linux-amd64.tar.gz
    stat ~/bin &>/dev/null || mkdir ~/bin
    mv k6-v0.51.0-linux-amd64/k6 ~/bin/
    chmod +x ~/bin/k6
    k6 --version
    ```
* SSH client - ssh, putty, etc.
  * generating SSH key in Azure Cloud Shell
    * run following command and for all following prompts just press Enter
      ```commandline
      ssh-keygen
      ```
* Some IDE (optional) - Visual Studio Code, PyCharm, IntelliJ IDEA, etc.

### Other Resources

* Open your team project in Azure DevOps: <hackathondomain>
* Clone your team's git repository (set the correct number of **your team**)
    * Use preferably SSH keys to authenticate or use credentials stored in your team Key Vault
    * GIT
      * `git clone git@github.com:lingea-research/azure-hackathon.git`
    * HTTPS
      * `git clone https://github.com/lingea-research/azure-hackathon.git`
* Modify your team's environment [file](scripts/hackathon.env) and source it in your shell. 

## Success Criteria

1. You have a zsh/bash shell with mentioned tools installed
1. Successfull cli login with your Microsoft account:
   * run `az login` and then use your hackathon MS account (`<first_name>.<last_name>@<hackathondomain>.onmicrosoft.com`)
   * run `az account show` to show information about your account and tenant
   * run `az account list -o table` to list available subscriptions
1. Locally cloned team's git repository
1. Running `echo $TEAM_NAME` displays your team name.

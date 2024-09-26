# Challenge 03 - Enable Azure AKS policy and enforce TLS on ingress object

 [< Previous Challenge](./challenge02.md) - **[Home](README.md)** - [Next Challenge >](./challenge04.md)

## Description

The Kubernetes environment is usually shared by different teams with varying levels of knowledge. To ensure the secure operation of applications, we must define how the objects we create in this cluster should look to avoid security risks.


## Success Criteria

1. Azure Policies are enabled on the cluster
2. Exclude cert-manager namespace from the policy assingment definition.
3. Ingress object in the namespace must be configured with `tls` section otherwise is rejected. 

## Learning Resources

- https://learn.microsoft.com/en-us/azure/governance/policy/concepts/policy-for-kubernetes
- https://www.tomaskubica.cz/post/2021/kubernetes-prakticky-bezpecnostni-politiky-s-azure-policy/

## Optional challenges
* Assign mandatory limits/request present in the AKS deployment definition. Please, be aware that wrong definition can cause rejects deployments. It's better to leave this challenge to the later phase of the hackathon :). After coach validation it is allowed delete the assignment back to the previous sate.

## Notes

Be careful, there is no special Azure policy specifically regarding ingress objects; instead, the policy name refers to enabling TLS for the entire cluster.

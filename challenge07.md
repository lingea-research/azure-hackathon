# Challenge 07 - Openai and Semantic Kernel

 [< Previous Challenge](./challenge06.md) - **[Home](README.md)** - [Next Challenge >](./challenge08.md)

## Description

Create your own chatbot capable of communicating with OpenAI and retrieving live data using OpenAI plugins. Use the prepared deployments with container images for the reference application "Chat Copilot."

## Chat Copilot deployment

For the OpenAI deployment, it is important to choose the right region based on the following matrix: https://learn.microsoft.com/en-gb/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability. Regions with GPT-4 model variants should be preferred.

For easier deployment of the Chat Copilot application, use prepared manifets on following link. Change all occurences of "CHANGEME", openai deployment names to actual values.

[link](./coach/k8s/challenge07/kustomization.yaml)

## Success Criteria

1. Chatbot is running on AKS
2. Chatbot is answering questions in web UI.

## Learning Resources

- [Semantic Kernel Overview](https://learn.microsoft.com/en-us/semantic-kernel/overview)
- [OpenAI plugins](https://azure.github.io/aihub/docs/openai-plugins/)
- [Chat Copilot - Reference application](https://learn.microsoft.com/en-us/semantic-kernel/chat-copilot/)
- [Sample OpenAI plugin](https://github.com/openai/plugins-quickstart)
- [RAG in Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)

## Optional challenges
1. The chatbot can identify and report the name of the AKS cluster where it is running using the prepared resource graph plugin.
2. Deploy an additional OpenAI plugin (either create your own or use an already prepared plugin).
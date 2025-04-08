# OpenSearch
Using AWS for opensearch Workshop

In this workshop, you will build an intelligent, multi-modal search application using Amazon OpenSearch Service and Generative AI. Attendees will learn to use Amazon Bedrock and LLMs with Amazon OpenSearch to create a holistic search experience for their organization without the need to have machine learning expertise.

You will start by deploying the web application and ingest a sample retail dataset. You will be augmenting the web application with every search type you learn throughout the workshop until you cover all search types supported by OpenSearch Service.

![image](https://github.com/user-attachments/assets/b3eb3129-9a0c-42e5-9d42-4d7cd53492ef)

In the first section, you will learn how to build a lexical search with OpenSearch Service and then deploy the lexical search into your web application and run few search queries.

In the second section, you will learn how to build Semantic search, Hybrid Search and Multimodal search with OpenSearch Service; and understand the associated value proposition.

In the last section of the workshop, you will build a conversational search leveraging foundation models (FMs) and retrieval-augmented generation (RAG) using the Vector engine of OpenSearch Serverless and Amazon Bedrock. Here, we will use Amazon Bedrock's Knowledge Base feature to create a chatbot.

Neural search in OpenSearch Service simplifies the translation of your data corpus and queries to vector embeddings, thereby removing much of the complexity of vector hydration and search. During ingestion, neural search transforms input data into vector embeddings and indexes the original data and the vector embeddings fields in a vector KNN index.

When you use a neural query during search, neural search converts the query text into vector embeddings, uses vector search to compare the query and document embeddings, and returns the closest results.

OpenSearch AI/ML connectors integrates with embedding models and LLMs hosted in third party ML platforms like SageMaker, Bedrock, OpenAI etc.

In this workshop, you will leverage ML models hosted in Amazon Bedrock and Amazon SageMaker. You will use Amazon Titan Models to generate text embeddings and multimodal embeddings via the OpenSearch AI/ML connector feature. OpenSearch AI/ML connector will enable you to connect to a Sparse model hosted in SageMaker to run neural sparse search in Lab 2 of this workshop.

The OpenSearch service AWS Console, provides AI/ML connectors blueprints to automates the model provisioning process for you. Once the ML model deployed in OpenSearch, you use the model ID to run neural search queries.

![image](https://github.com/user-attachments/assets/9de028e5-0ee7-4c91-8226-5e5bc59ffc23)

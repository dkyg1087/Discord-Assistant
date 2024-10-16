# Discord Assistant

**NOTE: THIS PROJECT IS STILL IN AN VERY EARLY STAGE OF DEVELOPMENT.**

## Project Overview

This repository hosts the code for a **Discord Assistant** that leverages LLM and various microservices to offer functionalities such as interacting with PDFs, performing grammar checks, and text rewriting. The architecture is designed to be modular, scalable, and deployed on Kubernetes, with all services communicating internally. The **Discord bot** serves as the primary user interface, allowing users to interact with different NLP-powered features.

### Objective

The primary goal of this project is to create a robust platform where users can interact with large language models (LLMs) through Discord. This involves:
- Using a locally run instance of LLM for generating responses based on user queries.
- Offering additional functionalities such as **grammar checks** and **text rewriting** via separate microservices.
- Enabling document upload (PDFs), parsing them into text, and allowing users to ask questions about the content.
- Supporting multiple LLM backends (like OpenAI) with the potential for future expansion.
- Additional features will be added.

**NOTE: THIS PROJECT IS STILL IN AN VERY EARLY STAGE OF DEVELOPMENT.**

While many of the core features are under development, this repository represents the early stages of the system architecture, service communication, and basic functionality. Additional services and improvements will be added as the project evolves.

## Features

- **Discord Bot Interface**: The bot serves as the user-facing interface, accepting user queries and routing them to the appropriate microservice.
- **LLaMA 3.2 Integration**: Uses the LLaMA 3.2 3B model for handling LLM-based tasks, including answering questions and providing summaries.
- **Grammar Check & Rewriting**: Separate service to handle grammar corrections and text rewriting tasks.
- **PDF Parsing**: Upload PDFs to the system, parse them, and allow interaction with the content.
- **Modular Architecture**: Each functionality is broken down into its own service to allow for easy maintenance, scaling, and future updates.

## Planned Enhancements

- Allow users to choose between different LLM backends, such as OpenAI’s GPT models, in case the local LLaMA service is unavailable.
- Add more NLP features and services that can be accessed via the Discord interface.
- Improve service communication and ensure reliable deployment on Kubernetes.
- Implement caching mechanisms to store parsed PDFs for faster retrieval.

## Current Architecture

The project is built around a **microservice architecture** with each service responsible for a specific task. Here's an overview:

1. **Discord Bot Service**: Handles communication with the user via Discord.
2. **LLM Service**: Processes text prompts using the LLaMA 3.2 3B model.
3. **Grammar & Rewrite Service**: Provides grammar correction and rewriting functionalities.
4. **PDF Parsing Service**: Manages the upload and parsing of PDFs, making them accessible for querying.
5. **Hugging Face Download Service** : Downloads models from Hugging Face if needed, making them available to the LLM service.

All services, except for the Discord bot, communicate internally through REST API calls within the Kubernetes environment.

## Deployment

The project is designed for deployment on **Kubernetes**, where each service runs as a separate pod. The Kubernetes manifests will manage service orchestration, scaling, and communication.

You can also run each service locally for development using **FastAPI** and Docker containers.

**NOTE: THIS PROJECT IS STILL IN AN VERY EARLY STAGE OF DEVELOPMENT.**

Some features may not be fully implemented or may undergo changes as development continues.

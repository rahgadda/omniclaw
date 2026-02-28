# Omniclaw: The Omnipotent Personal AI Orchestrator

![The Omnipotent Personal AI Orchestrator](./static/images/omniclaw.png)

## Overview

**Omniclaw** is a powerful, self-hosted AI agent designed to act as your proactive, personal orchestrator. It bridges the gap between conversational AI and automated execution, serving as a centralized hub that manages your digital environment from a single point of contact.

Built as an extension of the `openclaw` paradigm, Omniclaw is designed to reach out, grasp different endpoints, and manage complex, multi-step tasks across your system, all while adhering to the highest standards of privacy and control.

---

## Key Features

### 1. Unified Application Connectivity via MCP
Standardizes connections across different applications using the **Model Context Protocol**. Omniclaw effortlessly orchestrates REST APIs, local tools, and external services, synthesizing them into a unified, secure context for the AI agent to understand and interact with.

### 2. Proactive Job Scheduling
Transforms the agent from a reactive assistant into a proactive manager. Utilize integrated **Scheduled Jobs** (routines, cron jobs, delayed tasks) to automate routine activities silently in the background.

### 3. Dynamic Agent Skills
Leverages specialized **Agent Skills** that allow Omniclaw to execute complex requests. It doesn't just chat; it breaks down intricate user commands and performs multi-step executions across connected systems.

### 4. Multi-LLM Engine Support
Features an agnostic, flexible architecture with **Support for Multiple Large Language Models**. Deploy and configure different LLMs depending on the specific reasoning capability, speed, cost, or local inference requirements of the task at hand.

### 5. Multi-Gateway Accessibility
Designed to meet you where you already are. Access your personal orchestrator through popular messaging **Gateways** like **Telegram**, **WhatsApp**, or custom web interfaces, giving you omnipresent command of your digital world.

---

## Technical Architecture

The Omniclaw architecture follows a structured modular pattern, as visualised in the header diagram:

1.  **Gateways (Input/Output):** Secure entry points for user communication (e.g., Telegram Bot API).
2.  **Omniclaw Core:** The central brain responsible for parsing user intent, managing conversational memory, orchestrating skills, and dispatching scheduled tasks.
3.  **Agent Skills & Jobs Scheduler:** Modular execution components defining *how* tasks are performed and *when* they are triggered.
4.  **MCP Connectivity Layer:** The translation layer that allows the Core to interface standardly with diverse external applications (Databases, SaaS tools, etc.).
5.  **LLM Access Layer:** A robust middleware that routes inference requests to your configured Large Language Model providers.

---

## Getting Started



### Prerequisites

* Python 3.10+
* Docker (recommended)
* API keys for your chosen Gateways (e.g., Telegram Bot Token)
* Access to an LLM provider (local via Ollama/LocalAI or cloud via OpenAI/Anthropic/etc.)

### Installation



### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.


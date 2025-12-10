# TermInA

This project provides a complete, automated solution for installing and configuring Ollama on both Linux and Termux environments, allowing you to run language models either locally or from a remote machine. It is designed to simplify the deployment process so that users can quickly start interacting with models through the Ollama API.

At its core, the project includes a Python script that works as a lightweight wrapper client for Ollama. It sends prompts directly to the local API endpoint (http://localhost:11434) and displays responses using real-time streaming, providing an experience similar to modern LLM completion endpoints.

A key aspect of this tool is its intended use-case: it is designed for sending questions related to Linux commands, shell operations, CLI tools, and general terminal workflows. The integrated assistant, named TermInA, responds strictly with real, functional commands for Linux or Windows, avoiding fabricated libraries or non-existent functions. This makes the tool ideal for system administration, learning CLI environments, automation tasks, or quickly testing commands with an LLM that behaves predictably.

Key Features

Automated installation and setup of Ollama for Linux and Termux.

Use models locally or interact with them from a remote system.

Python wrapper script for sending prompts with streaming output.

Designed specifically for command-based queries, including Linux commands and CLI utilities.

TermInA assistant that returns only real, functional shell commands.

Great for developers, sysadmins, and users wanting a clean, predictable command-oriented LLM experience.

Example:
<img width="1440" height="850" alt="image" src="https://github.com/user-attachments/assets/d0f15d44-d237-482c-a887-d80f46a16827" />

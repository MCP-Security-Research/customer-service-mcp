
# 🏦 Banking Customer Service Model Context Protocol (MCP) Servers

> 💡 **Contains various example MCP Servers for testing that a financial institution could use for customer support.**

## Overview

This repository provides multiple examples of **Model Context Protocol (MCP) servers** for demonstrating the capabilities of an agentic banking customer support framework.

> **Note:** This is *not* a production-ready application and is intended for educational and demonstration purposes only. Security and authentication are not fully implemented; it is assumed that users are already authenticated.

This example includes an MCP server for each of the following banking customer support categories:

- 🚗 Auto Loan
- 💳 Credit Card
- 🏡 Home Equity Loan
- 🏠 Mortgage
- 📱 Online/Mobile Banking
- 💰 Personal Loan
- 🎓 Student Loan

## Requirements

To run the server, you will need:

- Python (recommended: 3.11+)
- [uv](https://github.com/uv-org/uv)
- Claude Desktop (for agent configuration)

## Setup Instructions

- **Create the example database:**

```bash
uv run src/database.py
```

- **Configure Claude Desktop:**

```text
- Open Claude Desktop.
- Go to `Settings` > `Developer` > `Edit Config`.
- Update the configuration to run from the absolute path to this repository.
```

```json
{
  "mcpServers": {
    "auto-loan-customer-support-agent": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/customer-service-mcp",
        "run",
        "-m",
        "src.categories.auto_loan"
      ]
    }
  }
}
```

To add additional MCP servers to this config, include more entries under the `mcpServers` object, for example:

- "credit-card-customer-support-agent"
- "home-equity-customer-support-agent"
- "mortgage-customer-support-agent"
- "online-mobile-banking-customer-support-agent"
- "personal-loan-customer-support-agent"
- "student-loan-customer-support-agent"

## Threat Vectors in General MCP Security

This repo is primarily used to demonstrate security issues that exist within MCP. It focuses on the following:

- 🧪 **Tool poisoning**: Malicious or compromised tools are injected into the agent's environment, causing it to perform unintended or harmful actions.
- 🕵️‍♂️ **Tool shadowing**: Legitimate tools are overridden or replaced by malicious versions, leading to unexpected or insecure behavior.

See the [ATTACKS.md](ATTACKS.md) document for more details.

## 🚀 Future Work

This repo is primarily for experimentation and prototyping.

**Improvement Ideas:**

- Implement function to dispute a charge on a credit card (send via mail)
- Implement function to request a replacement credit card (send via mail)
- Implement online banking "forgot password" flow (send via mail, update DB)
- Add ticket submission for cases where the model cannot determine the issue or needs more info (route to human review)
- Use SQLite and Claude Desktop for now; consider transitioning to a real application in the future
- MCP client: consider adding user info collection (maybe later)
- Remove the Claude Desktop config from the repo
- Add Python linting (e.g., ruff)

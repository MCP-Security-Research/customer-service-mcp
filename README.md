# Banking Customer Service Model Context Protocol (MCP) Servers

## Overview

This repository provides multiple examples of **model context protocol (mcp) servers** for demonstrating the capabilities of an agentic banking customer support framework. **Note:** This is *not* a production-ready application and is intended for educational and demonstration purposes only. Security and authentication are not fully implemented; it is assumed that users are already authenticated.

This example includes an example MCP server for each of the following banking customer support categories:

- Auto Loan
- Credit Card
- Home Equity Loan
- Mortgage
- Online/Mobile Banking
- Personal Loan
- Student Loan

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
    },
    // Add additional MCP servers to this config to access them in Claude Desktop:
    // "credit-card-customer-support-agent": { ... },
    // "home-equity-customer-support-agent": { ... },
    // "mortgage-customer-support-agent": { ... },
    // "online-mobile-banking-customer-support-agent": { ... },
    // "personal-loan-customer-support-agent": { ... },
    // "student-loan-customer-support-agent": { ...
  }
}
```

---

TODO List:

- function, disput charge on credit card --> mail
- function, request replacement credit card --> mail
- function, online banking forgot password --> mail, db
- also need something for submitting tickets (if the model cannot determine or needs more info, it will submit a ticket for a human to review.)!!!
- sql lite and claude desktop for now. could transition to real application
- mcp client --> can ask users for info, should i do this as well? maybe later on
- delete the claude desktop config
- add python linting like ruff

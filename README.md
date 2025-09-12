# Customer Service Model Context Protocol (MCP) Server

## Overview

The **Customer Service MCP Server** simulates a bank’s customer support automation system. It provides an interface for LLMs or other AI systems to send and receive messages (via email, SMS, or chat) on behalf of customer service agents. It also integrates with backend systems to fetch customer account information, log service tickets, and escalate cases.

The MCP server exposes tools/resources such as:

- **`send_message(customer_id, channel, message)`** – Sends an email, SMS, or chat message to a customer.
- **`get_customer_data(customer_id)`** – Retrieves customer profile, account details, and recent transactions.
- **`log_ticket(customer_id, issue_description)`** – Creates a service ticket.
- **`update_ticket(ticket_id, status)`** – Updates the status of a customer support ticket.
- **`fetch_email_inbox()`** – Retrieves incoming messages that need responses.

This makes it easy for a customer service AI assistant (running inside MCP) to interact with customers through messaging systems, fetch relevant data, and handle requests.

## Development Tools

- python
- uv
- mcp
- kubernetes cluster

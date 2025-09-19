# Banking Customer Service Model Context Protocol (MCP) Server

## Overview

bank customer support model context protocol agent

- send and receive messages (via email, SMS, or chat) on behalf of customer service agent
- It also integrates with backend systems to fetch customer account information, log service tickets, and escalate cases.
- simulate a database of customer profiles and tickets.
- common customer service issues

here are some example customer service categories that requests could be made under:

auto loans
home equity loans
mortgage
personal loans
student loans

credit cards
online and mobile banking
personal banking

-----
























## Development Tools

```json
example: claude_desktop_config.json
{
  "mcpServers": {
    "customer-service-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/aidandyga/Downloads/SeniorThesis/customer-service-mcp/src",
        "run",
        "server.py"
      ]
    }
  }
}
```

## xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

have multiple files. import the functions into a main server file. look into how these are built???
build it basically. then draw a diagram of how it works.

have multiple mcp servers. they all use some of the same functions in backedend and messaging.

sql lite and claude desktop for now. could transition to real application

requirements to run the server:

claude desktop

python x

uv x

and also do a setup guide

'''
overall description of how it will work here:

whenever a customer service request is made, the mcp will determine the intent of the request and route it to the appropriate file/function.

if the model cannot determine or needs more info, it will submit a ticket for a human to review.

assume that the user is already logged in to their account. but if you really wanted to you could 2fa before request is sent
'''

----

mcp client --> can ask users for info, should i do this as well? maybe later on

uv run src/database.py

"""FastMCP bank customer support model context protocol agent."""

'''
overall description of how it will work here:

whenever a customer service request is made, the mcp will determine the intent of the request and route it to the appropriate file/function.

if the model cannot determine or needs more info, it will submit a ticket for a human to review.

'''

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Bank Customer Support Agent")

# import the categories
# determine the intent of the users customer service request and route to the appropriate function

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

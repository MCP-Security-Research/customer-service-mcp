"""Provides answers to common mortgage questions."""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Mortgage Customer Support Agent")

@mcp.tool()
def mortgage_what_is_escrow() -> str:
    """Explains what escrow is in the context of a mortgage.

    Returns:
        str: Description of escrow accounts and their purpose in mortgage payments.
    """
    return (
        "Escrow is an account held by your lender to pay property taxes and insurance on your behalf. A portion of your monthly mortgage payment is deposited into the escrow account, and the lender uses these funds to pay your taxes and insurance when they are due."
    )

@mcp.tool()
def mortgage_setup_alerts() -> str:
    """Provides instructions on how to set up alerts for mortgage activity.

    Returns:
        str: Step-by-step guide for setting up mortgage alerts via online banking.
    """
    return (
        "To set up alerts for your mortgage, log in to your online banking account, go to the 'Alerts' or 'Notifications' section, and select your mortgage account. Choose the types of alerts you want to receive, such as payment due dates or account activity. You can customize how you receive alerts, including email, text, or push notifications."
    )

@mcp.tool()
def mortgage_schedule_payments() -> str:
    """Provides instructions on how to schedule mortgage payments.

    Returns:
        str: Step-by-step guide for scheduling one-time or recurring mortgage payments.
    """
    return (
        "To schedule payments for your mortgage, log in to your online or mobile banking, navigate to the 'Payments' section, select your mortgage account, and choose 'Schedule Payment.' You can set up one-time or recurring payments to ensure your mortgage is paid on time."
    )

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

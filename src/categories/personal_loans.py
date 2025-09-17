"""Provides answers to common personal loan questions."""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Personal Loan Customer Support Agent")

@mcp.tool()
def personal_loan_application_status() -> str:
    """Provides information on how to find the status of a personal loan application.

    Returns:
        str: Instructions for checking personal loan application status, including online steps and customer service contact.
    """
    return (
        "You can check your personal loan application status by logging into your online banking account, navigating to the 'Loans' section, and selecting 'Application Status.' For further assistance, contact our customer service at 1-800-000-0000."
    )

@mcp.tool()
def personal_loan_schedule_payment() -> str:
    """Provides instructions on how to schedule payments for a personal loan using another bank account.

    Returns:
        str: Step-by-step guide for scheduling personal loan payments, including linking external accounts.
    """
    return (
        "To schedule a payment for your personal loan, log in to your online or mobile banking, go to the 'Payments' section, select your personal loan account, and choose 'Schedule Payment.' You can set up payments from your account or link an external bank account."
    )

@mcp.tool()
def personal_loan_automated_vs_recurring() -> str:
    """Explains the difference between automated and recurring payments for personal loans.

    Returns:
        str: Description of automated payments versus recurring payments, including setup and management details.
    """
    return (
        "An automated payment is a payment that is automatically withdrawn from your account on a set date, often set up through your lender. A recurring payment is a payment you schedule to repeat at regular intervals, which you can manage or cancel through your online banking."
    )

@mcp.tool()
def personal_loan_stop_automated_payment() -> str:
    """Provides guidance on stopping an automated payment if funds are insufficient.

    Returns:
        str: Instructions for canceling or pausing an automated payment due to insufficient funds, including customer service contact and alternative actions.
    """
    return (
        "If you will not have enough funds for an upcoming automated payment, log in to your online banking and cancel or pause the payment, or contact customer service as soon as possible to avoid fees. You may also transfer funds into your account before the payment date."
    )

@mcp.tool()
def personal_loan_payoff_information() -> str:
    """Provides information on where to find personal loan payoff information.

    Returns:
        str: Instructions for finding personal loan payoff information online or via customer service.
    """
    return (
        "You can find your personal loan payoff information by logging into your online banking account and viewing your loan details. Alternatively, contact customer service to request a payoff quote."
    )

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

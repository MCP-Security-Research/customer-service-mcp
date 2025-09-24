"""Provides answers to common credit card questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_credit_card_expiration_date_by_number
import json

# Create an MCP server
mcp = FastMCP("Credit Card Customer Support Agent")

@mcp.tool()
def credit_card_lost_or_stolen() -> str:
    """Explains what to do if a credit card is lost or stolen.

    Returns:
        str: Instructions for reporting a lost or stolen credit card and next steps.
    """
    return (
        "If your credit card is lost or stolen, immediately report it by logging into your online banking account or calling customer service at 1-800-000-0000. Your card will be deactivated and a replacement will be issued. Monitor your account for unauthorized transactions."
    )

@mcp.tool()
def credit_card_request_replacement() -> str:
    """Provides instructions on requesting a replacement card if it is not working.

    Returns:
        str: Step-by-step guide for requesting a replacement credit card online or by phone.
    """
    return (
        "To request a replacement card, log in to your online banking account, go to the 'Cards' section, and select 'Request Replacement.' You can also call customer service to request a new card if your current one is damaged or not working."
    )

@mcp.tool()
def credit_card_make_payment() -> str:
    """Provides instructions on how to make a payment on a credit card.

    Returns:
        str: Step-by-step guide for making one-time or recurring credit card payments.
    """
    return (
        "To make a payment on your credit card, log in to your online or mobile banking, go to the 'Payments' section, select your credit card account, and choose 'Make Payment.' You can set up one-time or recurring payments from your bank account."
    )

@mcp.tool()
def credit_card_dispute_charge() -> str:
    """Explains how to dispute a charge on a credit card.

    Returns:
        str: Instructions for disputing a credit card charge online or via customer service.
    """
    return (
        "To dispute a charge, log in to your online banking account, find the transaction in your credit card activity, and select 'Dispute Transaction.' Follow the prompts to provide details. You can also contact customer service for assistance."
    )

@mcp.tool()
def credit_card_activate_new() -> str:
    """Provides instructions on how to activate a new credit card.

    Returns:
        str: Step-by-step guide for activating a new credit card online or by phone.
    """
    return (
        "To activate your new credit card, log in to your online banking account or call the activation number provided with your card. Follow the instructions to complete activation."
    )

@mcp.tool()
def credit_card_expiration_date(session: dict | str | None = None) -> str:
    """
    Checks the expiration date of a credit card by prompting for the card number if not provided.

    Args:
        session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

    Returns:
        str: JSON string containing the expiration date, or a prompt for the card number.
    """
    if session is None:
        session = {}
    if isinstance(session, str):
        session = json.loads(session)
    card_number = session.get('card_number')
    if not card_number:
        session['awaiting_card_number'] = True
        return json.dumps({"request": "Please provide your credit card number to check the expiration date.", "session": session})
    expiration = get_credit_card_expiration_date_by_number(card_number)
    if expiration is None:
        return json.dumps({"error": f"No credit card found for number {card_number}. Please check the number and try again.", "session": session})
    return json.dumps({"response": f"Your credit card (Number: {card_number}) expires on {expiration}.", "session": session})

@mcp.prompt()
def handle_credit_card_number_input(user_input: str, session: dict | str | None = None) -> str:
    """
    Handle user input for credit card number, store it in session/context, and return the expiration date.

    Args:
        user_input (str): The credit card number provided by the user.
        session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

    Returns:
        str: JSON string containing the expiration date or a prompt for the card number.
    """
    if session is None:
        session = {}
    if isinstance(session, str):
        session = json.loads(session)
    if session.get('awaiting_card_number'):
        session['card_number'] = user_input
        session.pop('awaiting_card_number', None)
        return credit_card_expiration_date(session)
    return credit_card_expiration_date(session)

@mcp.tool()
def credit_card_request_limit_increase() -> str:
    """Provides instructions on how to request a credit limit increase.

    Returns:
        str: Step-by-step guide for requesting a credit limit increase online or by phone.
    """
    return (
        "To request a credit limit increase, log in to your online banking account, go to the 'Cards' section, and select 'Request Credit Limit Increase.' You may need to provide updated income or employment information. You can also call customer service to make this request."
    )

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

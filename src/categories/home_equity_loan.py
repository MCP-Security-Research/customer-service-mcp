"""Provides answers to common home equity loan questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_application_status_by_type_and_number
import json

# Create an MCP server
mcp = FastMCP("Home Equity Loan Customer Support Agent")

@mcp.tool()
def home_equity_loan_application_status(session: dict | str | None = None) -> str:
	"""
	Checks the status of a home equity loan application by prompting for the loan number if not provided.

	Args:
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the home equity loan application, or a prompt for the loan number.
	"""
	# Initialize session if None
	if session is None:
		session = {}
	# If session is a string, parse it
	if isinstance(session, str):
		session = json.loads(session)
	# Check if loan_number is already in session/context
	loan_number = session.get('loan_number')
	if not loan_number:
		# Prompt user for loan number and store in session/context
		session['awaiting_loan_number'] = True
		return json.dumps({"request": "Please provide your home equity loan number to check the application status.", "session": session})

	# If loan_number is provided, call the DB function
	result = get_application_status_by_type_and_number("home_equity", loan_number)
	if result is None:
		return json.dumps({"error": f"No application found for loan number {loan_number}. Please check the number and try again.", "session": session})
	status = result['status']
	loan_type = result['loan_type']
	return json.dumps({"response": f"Your {loan_type} loan application (Loan Number: {loan_number}) is currently in '{status}' status.", "session": session})


@mcp.prompt()
def handle_home_equity_loan_number_input(user_input: str, session: dict | str | None = None) -> str:
	"""
	Handle user input for home equity loan number, store it in session/context, and return the application status.

	Args:
		user_input (str): The loan number provided by the user.
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the home equity loan application or a prompt for the loan number.
	"""
	# Initialize session if None
	if session is None:
		session = {}
	# If session is a string, parse it
	if isinstance(session, str):
		session = json.loads(session)
	if session.get('awaiting_loan_number'):
		session['loan_number'] = user_input
		session.pop('awaiting_loan_number', None)
		return home_equity_loan_application_status(session)
	# If not awaiting loan number, just return the status tool (fallback)
	return home_equity_loan_application_status(session)

@mcp.tool()
def home_equity_loan_fees() -> str:
    """Provides information about fees associated with home equity loans.

    Returns:
        str: Description of possible fees for home equity loans and where to find more details.
    """
    return (
        "There may be fees associated with home equity loans, such as application fees, appraisal fees, and closing costs. For a detailed breakdown of fees, please review your loan documents or contact our customer service at 1-800-000-0000."
    )

@mcp.tool()
def home_equity_loan_application() -> str:
    """Provides instructions on how to apply for a home equity loan.

    Returns:
        str: Step-by-step guide for applying for a home equity loan online, in-branch, or by phone.
    """
    return (
        "To apply for a home equity loan, log in to your online banking account and navigate to the 'Loans' section. Select 'Apply for Home Equity Loan' and follow the on-screen instructions. You can also apply by visiting a branch or calling customer service."
    )

@mcp.tool()
def home_equity_loan_usage() -> str:
    """Explains what a home equity loan can be used for.

    Returns:
        str: List of common uses for home equity loans and a recommendation to consult a financial advisor.
    """
    return (
        "A home equity loan can be used for a variety of purposes, including home improvements, debt consolidation, education expenses, or major purchases. Please consult with a financial advisor to determine if a home equity loan is right for your needs."
    )

@mcp.tool()
def home_equity_loan_interest_rate() -> str:
    """Provides information on where to find the interest rate for a home equity loan.

    Returns:
        str: Instructions for finding your home equity loan interest rate online or in your loan documents.
    """
    return (
        "You can find your home equity loan interest rate by logging into your online banking account and viewing your loan details. The interest rate is also listed on your loan agreement documents. For further assistance, contact customer service."
    )

@mcp.tool()
def home_equity_loan_make_payment() -> str:
    """Provides instructions on how to make a payment on a home equity loan.

    Returns:
        str: Step-by-step guide for making one-time or recurring payments on a home equity loan.
    """
    return (
        "To make a payment on your home equity loan, log in to your online or mobile banking, go to the 'Payments' section, select your home equity loan account, and choose 'Make Payment.' You can set up one-time or recurring payments."
    )

@mcp.tool()
def home_equity_loan_payment_history() -> str:
    """Explains how to view payment history for a home equity loan.

    Returns:
        str: Instructions for viewing payment history online or requesting a statement from customer service.
    """
    return (
        "To view your payment history for your home equity loan, log in to your online banking account, select your home equity loan account, and navigate to the 'Payment History' section. You can also request a statement from customer service."
    )

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

"""Provides answers to common auto loan questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_application_status_by_type_and_number
import json

# Create an MCP server
mcp = FastMCP("Auto Loan Customer Support Agent")

@mcp.tool()
def auto_loan_application_status(session: dict | str | None = None) -> str:
	"""
	Checks the status of an auto loan application by prompting for the loan number if not provided.

	Args:
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the auto loan application, or a prompt for the loan number.
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
		return json.dumps({"request": "Please provide your auto loan number to check the application status.", "session": session})

	# If loan_number is provided, call the DB function
	result = get_application_status_by_type_and_number("auto", loan_number)
	if result is None:
		return json.dumps({"error": f"No application found for loan number {loan_number}. Please check the number and try again.", "session": session})
	status = result['status']
	loan_type = result['loan_type']
	return json.dumps({"response": f"Your {loan_type} loan application (Loan Number: {loan_number}) is currently in '{status}' status.", "session": session})

@mcp.prompt()
def handle_auto_loan_number_input(user_input: str, session: dict | str | None = None) -> str:
	"""
	Handle user input for loan number, store it in session/context, and return the application status.

	Args:
		user_input (str): The loan number provided by the user.
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the auto loan application or a prompt for the loan number.
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
		return auto_loan_application_status(session)
	# If not awaiting loan number, just return the status tool (fallback)
	return auto_loan_application_status(session)

@mcp.tool()
def auto_loan_schedule_payment() -> str:
	"""Provides instructions on how to schedule payments for an auto loan.

	Returns:
		str: Step-by-step guide for scheduling one-time or recurring auto loan payments via online or mobile banking.
	"""
	return (
		"To schedule a payment for your auto loan, log in to your online or mobile banking, go to the 'Payments' section, select your auto loan account, and choose 'Schedule Payment.' You can set up one-time or recurring payments."
	)

@mcp.tool()
def auto_loan_automated_recurring_payments() -> str:
	"""Explains the difference between automated and recurring auto loan payments.

	Returns:
		str: Description of automated payments versus recurring payments, including setup and management details.
	"""
	return (
		"An automated payment is a payment that is automatically withdrawn from your account on a set date, often set up through your lender. A recurring payment is a payment you schedule to repeat at regular intervals, which you can manage or cancel through your online banking."
	)

@mcp.tool()
def insufficient_funds_stop_auto_loan_automated_payment() -> str:
	"""Provides guidance on stopping an automated auto loan payment if there are insufficient funds.

	Returns:
		str: Instructions for canceling or pausing an automated payment due to insufficient funds, including customer service contact and alternative actions.
	"""
	return (
		"If you do not have enough funds for an upcoming automated payment, log in to your online banking and cancel or pause the payment, or contact customer service as soon as possible to avoid fees. You may also transfer funds into your account before the payment date."
	)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

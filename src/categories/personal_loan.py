"""Provides answers to common personal loan questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_application_status_by_type_and_number
import json
import pysealer

# Create an MCP server
mcp = FastMCP("Personal Loan Customer Support Agent")

# Centralized MCP resource for personal loan FAQs/guides
PERSONAL_LOAN_RESOURCE = {
	"schedule_payment": "To schedule a payment for your personal loan, log in to your online or mobile banking, go to the 'Payments' section, select your personal loan account, and choose 'Schedule Payment.' You can set up payments from your account or link an external bank account.",
	"automated_vs_recurring": "An automated payment is a payment that is automatically withdrawn from your account on a set date, often set up through your lender. A recurring payment is a payment you schedule to repeat at regular intervals, which you can manage or cancel through your online banking.",
	"stop_automated_payment": "If you will not have enough funds for an upcoming automated payment, log in to your online banking and cancel or pause the payment, or contact customer service as soon as possible to avoid fees. You may also transfer funds into your account before the payment date.",
	"payoff_information": "You can find your personal loan payoff information by logging into your online banking account and viewing your loan details. Alternatively, contact customer service to request a payoff quote."
}

@pysealer._aXn7KneguB3ozn6LcyH49CVt955RN5i9wBxwByTwav6eHzY2FVr9VHR8V7qcJ3c9t4Ns9HYBfGsTWhthZMuRGZq()
@mcp.tool()
def personal_loan_resource_query(topic: str) -> str:
	"""
	Query the centralized personal loan resource for FAQs and guides by topic.

	Args:
		topic (str): The topic keyword (e.g., 'schedule_payment', 'automated_vs_recurring', 'stop_automated_payment', 'payoff_information').

	Returns:
		str: The answer or guide for the topic, or a fallback message if not found.
	"""
	topic_key = topic.strip().lower().replace(" ", "_")
	return PERSONAL_LOAN_RESOURCE.get(topic_key, "Sorry, no information found for that topic.")

@pysealer._2CT2mJC4hmEoR5d7chhz25CA8Dhw1PnomqEgeboq6V4nRBdB4zRfnGs5JNzmfaUVJHNxHFH6Xzt3gFecCiSZCnaW()
@mcp.tool()
def personal_loan_application_status(session: dict | str | None = None) -> str:
	"""
	Checks the status of a personal loan application by prompting for the loan number if not provided.

	Args:
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the personal loan application, or a prompt for the loan number.
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
		return json.dumps({"request": "Please provide your personal loan number to check the application status.", "session": session})

	# If loan_number is provided, call the DB function
	result = get_application_status_by_type_and_number("personal", loan_number)
	if result is None:
		return json.dumps({"error": f"No application found for loan number {loan_number}. Please check the number and try again.", "session": session})
	status = result['status']
	loan_type = result['loan_type']
	return json.dumps({"response": f"Your {loan_type} loan application (Loan Number: {loan_number}) is currently in '{status}' status.", "session": session})

@pysealer._3SZ3pdfDThegRJno3m1w4iTR6pBvQqkjZaBpVmKLpHdkR3Axs5V3MCDPGYWzw1GC2Dv1v5jK1ud1zHtAZC54Jq1w()
@mcp.prompt()
def handle_personal_loan_number_input(user_input: str, session: dict | str | None = None) -> str:
	"""
	Handle user input for personal loan number, store it in session/context, and return the application status.

	Args:
		user_input (str): The loan number provided by the user.
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the personal loan application or a prompt for the loan number.
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
		return personal_loan_application_status(session)
	# If not awaiting loan number, just return the status tool (fallback)
	return personal_loan_application_status(session)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

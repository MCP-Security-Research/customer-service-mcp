"""Provides answers to common home equity loan questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_application_status_by_type_and_number
import json
import pysealer

# Create an MCP server
mcp = FastMCP("Home Equity Loan Customer Support Agent")

# Centralized MCP resource for home equity loan FAQs/guides
HOME_EQUITY_LOAN_RESOURCE = {
	"fees": "There may be fees associated with home equity loans, such as application fees, appraisal fees, and closing costs. For a detailed breakdown of fees, please review your loan documents or contact our customer service at 1-800-000-0000.",
	"application": "To apply for a home equity loan, log in to your online banking account and navigate to the 'Loans' section. Select 'Apply for Home Equity Loan' and follow the on-screen instructions. You can also apply by visiting a branch or calling customer service.",
	"usage": "A home equity loan can be used for a variety of purposes, including home improvements, debt consolidation, education expenses, or major purchases. Please consult with a financial advisor to determine if a home equity loan is right for your needs.",
	"interest_rate": "You can find your home equity loan interest rate by logging into your online banking account and viewing your loan details. The interest rate is also listed on your loan agreement documents. For further assistance, contact customer service.",
	"make_payment": "To make a payment on your home equity loan, log in to your online or mobile banking, go to the 'Payments' section, select your home equity loan account, and choose 'Make Payment.' You can set up one-time or recurring payments.",
	"payment_history": "To view your payment history for your home equity loan, log in to your online banking account, select your home equity loan account, and navigate to the 'Payment History' section. You can also request a statement from customer service."
}

@pysealer._4DzkjwfLm8zP5y1ZgYfJdMshmenbvNYUxGEH9xKvpg7Fhpx2w2oaFwx9SBvMacpzBTS21MwujbmyB3Ljd9G98NKB()
@mcp.tool()
def home_equity_loan_resource_query(topic: str) -> str:
	"""
	Query the centralized home equity loan resource for FAQs and guides by topic.

	Args:
		topic (str): The topic keyword (e.g., 'fees', 'application', 'usage', 'interest_rate', 'make_payment', 'payment_history').

	Returns:
		str: The answer or guide for the topic, or a fallback message if not found.
	"""
	topic_key = topic.strip().lower().replace(" ", "_")
	return HOME_EQUITY_LOAN_RESOURCE.get(topic_key, "Sorry, no information found for that topic.")

@pysealer._3E327SmA9pyvjVs3Q73xMTsvHT3Pv7mEizoZX3zrfDqR6njbKmjT75WSedWy7AkXSrbzqc4vbwhxxUkshUrygQfy()
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

@pysealer._3npaVJLvoggLgai6Gh7pCwyLpqn2zmgKyt5bKd65Ti598V49Cngj5c4i4uvKLc3K4HKZRb2e4qhqTqcVyoN7L76G()
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
	if session is None:
		session = {}
	if isinstance(session, str):
		session = json.loads(session)
	if session.get('awaiting_loan_number'):
		session['loan_number'] = user_input
		session.pop('awaiting_loan_number', None)
		return home_equity_loan_application_status(session)
	# If not awaiting loan number, just return the status tool (fallback)
	return home_equity_loan_application_status(session)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

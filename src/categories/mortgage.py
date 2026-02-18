"""Provides answers to common mortgage questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_application_status_by_type_and_number
import json
import pysealer

# Create an MCP server
mcp = FastMCP("Mortgage Customer Support Agent")

# Centralized MCP resource for mortgage FAQs/guides
MORTGAGE_RESOURCE = {
	"what_is_escrow": "Escrow is an account held by your lender to pay property taxes and insurance on your behalf. A portion of your monthly mortgage payment is deposited into the escrow account, and the lender uses these funds to pay your taxes and insurance when they are due.",
	"setup_alerts": "To set up alerts for your mortgage, log in to your online banking account, go to the 'Alerts' or 'Notifications' section, and select your mortgage account. Choose the types of alerts you want to receive, such as payment due dates or account activity. You can customize how you receive alerts, including email, text, or push notifications.",
	"schedule_payments": "To schedule payments for your mortgage, log in to your online or mobile banking, navigate to the 'Payments' section, select your mortgage account, and choose 'Schedule Payment.' You can set up one-time or recurring payments to ensure your mortgage is paid on time."
}

@pysealer._5aupJjnASGh2hdsBqzd918KsznQtGpuLU4VMSG2hAYHSep2npFj7zUgoQANhvWDBnyfZKjV7cM9Wb88FsN7We7CM()
@mcp.tool()
def mortgage_resource_query(topic: str) -> str:
	"""
	Query the centralized mortgage resource for FAQs and guides by topic.

	Args:
		topic (str): The topic keyword (e.g., 'what_is_escrow', 'setup_alerts', 'schedule_payments').

	Returns:
		str: The answer or guide for the topic, or a fallback message if not found.
	"""
	topic_key = topic.strip().lower().replace(" ", "_")
	return MORTGAGE_RESOURCE.get(topic_key, "Sorry, no information found for that topic.")

@pysealer._4Q9PUccwTQsAZLmGTLpG1UWDay35ePw3XAghRhrqg37hfoLLsdNGTFpxECMegRNUv9BfJCKzMSadwPMBcJJvrdW8()
@mcp.tool()
def mortgage_application_status(session: dict | str | None = None) -> str:
	"""
	Checks the status of a mortgage application by prompting for the loan number if not provided.

	Args:
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the mortgage application, or a prompt for the loan number.
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
		return json.dumps({"request": "Please provide your mortgage loan number to check the application status.", "session": session})

	# If loan_number is provided, call the DB function
	result = get_application_status_by_type_and_number("mortgage", loan_number)
	if result is None:
		return json.dumps({"error": f"No application found for mortgage loan number {loan_number}. Please check the number and try again.", "session": session})
	status = result['status']
	loan_type = result['loan_type']
	return json.dumps({"response": f"Your {loan_type} loan application (Loan Number: {loan_number}) is currently in '{status}' status.", "session": session})

@pysealer._49xLj3tTjJ1CNYMBKshSdSHAkRxmCge9QBXXL3UqLYWoh28qzA1mYFjT2MENk1T7Vp74hRaYsgNVutGkqeiJRNnt()
@mcp.prompt()
def handle_mortgage_loan_number_input(user_input: str, session: dict | str | None = None) -> str:
	"""
	Handle user input for mortgage loan number, store it in session/context, and return the application status.

	Args:
		user_input (str): The mortgage loan number provided by the user.
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.
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
		return mortgage_application_status(session)
	# If not awaiting loan number, just return the status tool (fallback)
	return mortgage_application_status(session)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

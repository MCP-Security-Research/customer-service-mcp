"""Provides answers to common auto loan questions."""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Auto Loan Customer Support Agent")

@mcp.tool()
def auto_loan_application_status() -> str:
	"""Provides information on how to find the status of an auto loan application.

	Returns:
		str: Instructions for checking auto loan application status, including online steps and customer service contact.
	"""
	return (
		"You can check your auto loan application status by logging into your online banking account, navigating to the 'Loans' section, and selecting 'Application Status.' If you need further assistance, contact our customer service at 1-800-000-0000."
	)

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

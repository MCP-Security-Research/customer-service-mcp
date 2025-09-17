"""Provides answers to common online and mobile banking questions."""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Online and Mobile Banking Customer Support Agent")

@mcp.tool()
def set_up_alerts() -> str:
	"""Provides instructions on how to set up alerts for your account.

	Returns:
		str: Step-by-step guide for setting up account alerts via online banking.
	"""
	return (
		"To set up alerts for your account, log in to your online banking, go to the 'Alerts' section, and select the types of alerts you want to receive."
	)

@mcp.tool()
def browser_requirements() -> str:
	"""Lists the browser requirements for Online Banking.

	Returns:
		str: Supported browsers and versions for Online Banking.
	"""
	return (
		"Online Banking supports the latest versions of Chrome, Firefox, Safari, and Edge. Ensure your browser is up to date for the best experience."
	)

@mcp.tool()
def online_banking_capabilities() -> str:
	"""Describes what you can do in Online Banking.

	Returns:
		str: Overview of features and capabilities available in Online Banking.
	"""
	return (
		"In Online Banking, you can view account balances, transfer funds, pay bills, view statements, and manage your account settings."
	)

@mcp.tool()
def compromised_or_unauthorized_activity() -> str:
	"""Explains what to do if your Online Banking information is compromised or you notice unauthorized activity.

	Returns:
		str: Steps to take if you suspect fraud or unauthorized access.
	"""
	return (
		"If you suspect your Online Banking information is compromised, change your password immediately and contact customer service."
	)

@mcp.tool()
def required_pin_for_enrollment() -> str:
	"""Explains what PIN number is needed to enroll for Online Banking.

	Returns:
		str: Information about the required PIN for Online Banking enrollment.
	"""
	return (
		"You will need the PIN provided at account opening or mailed to you to enroll for Online Banking."
	)

@mcp.tool()
def forgot_password_or_user_id() -> str:
	"""Explains what to do if you forgot your Online Banking password or user ID.

	Returns:
		str: Steps to recover or reset your Online Banking credentials.
	"""
	return (
		"Use the 'Forgot Password' or 'Forgot User ID' links on the Online Banking login page to reset your credentials."
	)

@mcp.tool()
def transfer_funds() -> str:
	"""Provides instructions on how to transfer funds in Online Banking.

	Returns:
		str: Step-by-step guide for transferring funds between accounts.
	"""
	return (
		"To transfer funds, log in to Online Banking, select 'Transfer Funds,' choose the accounts, enter the amount, and confirm the transfer."
	)

@mcp.tool()
def get_check_copy_online() -> str:
	"""Explains how to get a copy of a check online.

	Returns:
		str: Instructions for obtaining check copies through Online Banking.
	"""
	return (
		"To get a copy of a check, log in to Online Banking, find the transaction in your account history, and select 'View Check Image.'"
	)

@mcp.tool()
def get_statements_online() -> str:
	"""Provides instructions on how to get copies of statements online.

	Returns:
		str: Steps to access and download account statements in Online Banking.
	"""
	return (
		"To get copies of your statements, log in to Online Banking, go to the 'Statements' section, and download the desired statement."
	)

@mcp.tool()
def enrollment_timing() -> str:
	"""Explains when you can enroll for Online Banking after opening an account.

	Returns:
		str: Information on when new account holders can enroll for Online Banking.
	"""
	return (
		"You can enroll for Online Banking as soon as your account is active, usually within one business day of opening."
	)

@mcp.tool()
def endorse_check_for_mobile_deposit() -> str:
	"""Explains how to properly endorse a check for Mobile Deposit.

	Returns:
		str: Instructions for endorsing checks for mobile deposit.
	"""
	return (
		"To endorse a check for Mobile Deposit, sign the back and write 'For Mobile Deposit Only' below your signature."
	)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

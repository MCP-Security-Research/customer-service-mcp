"""Provides answers to common online and mobile banking questions."""

from mcp.server.fastmcp import FastMCP
import pysealer

# Create an MCP server
mcp = FastMCP("Online and Mobile Banking Customer Support Agent")

# Centralized MCP resource for online and mobile banking FAQs/guides
ONLINE_MOBILE_BANKING_RESOURCE = {
	"set_up_alerts": "To set up alerts for your account, log in to your online banking, go to the 'Alerts' section, and select the types of alerts you want to receive.",
	"browser_requirements": "Online Banking supports the latest versions of Chrome, Firefox, Safari, and Edge. Ensure your browser is up to date for the best experience.",
	"online_banking_capabilities": "In Online Banking, you can view account balances, transfer funds, pay bills, view statements, and manage your account settings.",
	"compromised_or_unauthorized_activity": "If you suspect your Online Banking information is compromised, change your password immediately and contact customer service.",
	"required_pin_for_enrollment": "You will need the PIN provided at account opening or mailed to you to enroll for Online Banking.",
	"forgot_password_or_user_id": "Use the 'Forgot Password' or 'Forgot User ID' links on the Online Banking login page to reset your credentials.",
	"transfer_funds": "To transfer funds, log in to Online Banking, select 'Transfer Funds,' choose the accounts, enter the amount, and confirm the transfer.",
	"get_check_copy_online": "To get a copy of a check, log in to Online Banking, find the transaction in your account history, and select 'View Check Image.'",
	"get_statements_online": "To get copies of your statements, log in to Online Banking, go to the 'Statements' section, and download the desired statement.",
	"enrollment_timing": "You can enroll for Online Banking as soon as your account is active, usually within one business day of opening.",
	"endorse_check_for_mobile_deposit": "To endorse a check for Mobile Deposit, sign the back and write 'For Mobile Deposit Only' below your signature."
}

@pysealer._2tmFAcLML12VQpN5pv8tgPbrb9hTXH74mQDGY22ZEb1mMNM3efDrM39WzhuhDNdD4zkPhcQhCRoAoLpTbuzRknpq()
@mcp.tool()
def online_mobile_banking_resource_query(topic: str) -> str:
	"""
	Query the centralized online/mobile banking resource for FAQs and guides by topic.

	Args:
		topic (str): The topic keyword (e.g., 'set_up_alerts', 'browser_requirements', 'online_banking_capabilities', ...).

	Returns:
		str: The answer or guide for the topic, or a fallback message if not found.
	"""
	topic_key = topic.strip().lower().replace(" ", "_")
	return ONLINE_MOBILE_BANKING_RESOURCE.get(topic_key, "Sorry, no information found for that topic.")

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

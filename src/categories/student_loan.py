"""Provides answers to common student loan questions."""

from mcp.server.fastmcp import FastMCP
from src.backend import get_application_status_by_type_and_number
import json

# Create an MCP server
mcp = FastMCP("Student Loan Customer Support Agent")

@mcp.tool()
def student_loan_application_status(session: dict | str | None = None) -> str:
	"""
	Checks the status of a student loan application by prompting for the loan number if not provided.

	Args:
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the student loan application, or a prompt for the loan number.
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
		return json.dumps({"request": "Please provide your student loan number to check the application status.", "session": session})

	# If loan_number is provided, call the DB function
	result = get_application_status_by_type_and_number("student", loan_number)
	if result is None:
		return json.dumps({"error": f"No application found for loan number {loan_number}. Please check the number and try again.", "session": session})
	status = result['status']
	loan_type = result['loan_type']
	return json.dumps({"response": f"Your {loan_type} loan application (Loan Number: {loan_number}) is currently in '{status}' status.", "session": session})


@mcp.prompt()
def handle_student_loan_number_input(user_input: str, session: dict | str | None = None) -> str:
	"""
	Handle user input for student loan number, store it in session/context, and return the application status.

	Args:
		user_input (str): The loan number provided by the user.
		session (dict | str | None): MCP session/context for storing user state. Can be a dict, str (JSON), or None.

	Returns:
		str: JSON string containing the status of the student loan application or a prompt for the loan number.
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
		return student_loan_application_status(session)
	# If not awaiting loan number, just return the status tool (fallback)
	return student_loan_application_status(session)

@mcp.tool()
def student_loan_eligibility_requirements() -> str:
    """Provides information about eligibility requirements for student loans.

    Returns:
        str: List of typical eligibility requirements for student loans.
    """
    return (
        "Eligibility requirements for student loans typically include being enrolled at least half-time in an eligible educational program, being a U.S. citizen or eligible non-citizen, and maintaining satisfactory academic progress. Additional requirements may apply depending on the loan type."
    )

@mcp.tool()
def student_loan_application() -> str:
    """Provides instructions on how to apply for a student loan.

    Returns:
        str: Step-by-step guide for applying for federal and private student loans.
    """
    return (
        "To apply for a student loan, complete the Free Application for Federal Student Aid (FAFSA) online at fafsa.gov. You may also apply for private student loans through your bank or lender's website. Contact your school's financial aid office for more information."
    )

@mcp.tool()
def student_loan_interest_rate() -> str:
    """Provides information about the interest rate on student loans.

    Returns:
        str: Explanation of how student loan interest rates are determined and where to find your rate.
    """
    return (
        "The interest rate on student loans depends on the type of loan and when it was disbursed. Federal student loan rates are set by the government and may change annually. Private loan rates vary by lender. Check your loan documents or contact your lender for your specific interest rate."
    )

@mcp.tool()
def student_loan_repayment_start() -> str:
    """Explains when repayment of student loans begins.

    Returns:
        str: Information on when repayment starts for federal and private student loans.
    """
    return (
        "Repayment of most federal student loans begins six months after you graduate, leave school, or drop below half-time enrollment. Private loan repayment terms may vary. Review your loan agreement or contact your lender for details."
    )

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

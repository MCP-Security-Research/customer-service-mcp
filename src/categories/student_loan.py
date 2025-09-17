"""Provides answers to common student loan questions."""

from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Student Loan Customer Support Agent")

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

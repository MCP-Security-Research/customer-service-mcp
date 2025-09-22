"""Backend functions for gathering customer information for customer support purposes."""

'''
the table is named customer_info.db and is located in the base directory of the project.
functions i need:

all application status --> prompt back for loan type and number, then check if the loan is in the pending state, or active state --> db
x
disput charge on credit card --> mail
request replacement credit card --> mail
credit card experation date --> db
x
online banking forgot password --> mail, db
'''

import sqlite3
import os

def get_application_status_by_number(loan_number):
    """
    Retrieve the status and type of a loan application by loan number.

    Args:
        loan_number (str): The unique loan number to look up.

    Returns:
        dict or None: A dictionary with keys 'status', 'loan_type', and 'loan_number' if found, otherwise None.
    """
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'customer_info.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    status_map = {0: 'pending', 1: 'active'}
    cursor.execute("""
        SELECT loan_type, is_active, loan_number FROM loans
        WHERE loan_number = ? AND is_active IN (0, 1)
    """, (loan_number,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            'loan_type': row[0],
            'status': status_map.get(row[1], 'unknown'),
            'loan_number': row[2]
        }
    else:
        return None

"""Backend functions for gathering customer information for customer support purposes."""

'''
functions i need:
x
disput charge on credit card --> mail
request replacement credit card --> mail
credit card experation date --> db
x
online banking forgot password --> mail, db
'''

import sqlite3
import os

def get_application_status_by_type_and_number(loan_type: str, loan_number: str) -> dict | None:
    """
    Retrieve the status and type of a loan application by loan type and loan number.

    Args:
        loan_type (str): The type of loan to look up (e.g., 'auto', 'credit_card').
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
        WHERE loan_type = ? AND loan_number = ? AND is_active IN (0, 1)
    """, (loan_type, loan_number))
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

def get_credit_card_expiration_date_by_number(card_number: str) -> str | None:
    """
    Retrieve the expiration date of a credit card by card number.

    Args:
        card_number (str): The credit card number to look up.

    Returns:
        str or None: The expiration date as a string (e.g., '2027-12-31') if found, otherwise None.
    """
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'customer_info.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT expiration_date FROM credit_cards
        WHERE card_number = ?
    """, (card_number,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    else:
        return None

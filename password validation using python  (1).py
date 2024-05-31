#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


import re

print("Welcome to login Form!")
username = input("Enter your username: ")
# Check if username contains only alphanumeric characters and underscores
if re.match(r"^[a-zA-Z0-9_]+$", username):
    print("Valid username")
else:
    print("Please choose a valid username containing only alphanumeric characters and underscores.")
    print("""The username should only contain:
    - Uppercase letters
    - Lowercase letters
    - Underscores
    - Numeric values
    Note: No other special characters should be used!
    Try again.
    """)
    
password = input("Enter your password: ")

# Check for password validity
valid = True

if not re.search(r"[a-z]", password):
    print("Please enter at least one lowercase alphabet!")
    valid = False

if not re.search(r"[A-Z]", password):
    print("Please enter at least one uppercase alphabet!")
    valid = False

if len(password) < 8:
    print("The password must be at least 8 characters long!")
    valid = False

if not re.search(r"[!@$%^&*()\-_+=\[\]{}|\\;:'\",.<>?/]", password):
    print("Please enter at least one special character!")
    valid = False

if not re.search(r"\d", password):
    print("Please enter at least one digit!")
    valid = False

if valid:
    print("Valid password. Your password is:", password)
    print("Login saved!")
else:
    print("Please enter a valid password.")
    


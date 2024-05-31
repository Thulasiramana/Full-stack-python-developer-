#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


# Dictionary to hold user credentials
users = {}

def register():
    print("Welcome to the Registration Page!")
    username = input("Enter your desired username: ")
    
    # Check if username is already taken
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    
    password = input("Enter your desired password: ")
    users[username] = password
    print("Registration successful! You can now login.")

def login():
    print("Welcome to the Login Page!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username exists
    if username in users:
        # Check if the password matches
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please register or try again.")

def main():
    while True:
        choice = input("Do you want to register (r) or login (l)? (r/l): ")
        if choice.lower() == "r":
            register()
        elif choice.lower() == "l":
            login()
        else:
            print("Invalid choice. Please select 'r' for register or 'l' for login.")
        
        again = input("Do you want to perform another action? (yes/no): ")
        if again.lower() != "yes":
            print("Thank you for using our system.")
            break

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





# In[ ]:





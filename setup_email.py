#!/usr/bin/env python3
"""
Quick Email Setup Script
Run this to configure your email credentials
"""

import re

def setup_email():
    print("=== Email Setup for Smart Study Platform ===\n")
    
    # Get email address
    while True:
        email = input("Enter your Gmail address: ").strip()
        if re.match(r'^[a-zA-Z0-9._%+-]+@gmail\.com$', email):
            break
        print("Please enter a valid Gmail address (e.g., john@gmail.com)")
    
    # Get app password
    while True:
        password = input("Enter your Gmail App Password (16 chars): ").strip().replace(' ', '')
        if len(password) == 16 and password.isalnum():
            break
        print("App password should be 16 characters (letters and numbers only)")
    
    # Update app.py file
    try:
        with open('app.py', 'r') as f:
            content = f.read()
        
        # Replace email credentials
        content = content.replace("EMAIL_ADDRESS = 'your_email@gmail.com'", f"EMAIL_ADDRESS = '{email}'")
        content = content.replace("EMAIL_PASSWORD = 'your_app_password'", f"EMAIL_PASSWORD = '{password}'")
        
        with open('app.py', 'w') as f:
            f.write(content)
        
        print(f"\n✅ Email configured successfully!")
        print(f"📧 Email: {email}")
        print(f"🔑 Password: {'*' * len(password)}")
        print(f"\nYou can now send real emails through the platform!")
        
    except Exception as e:
        print(f"❌ Error updating configuration: {e}")

if __name__ == "__main__":
    setup_email()
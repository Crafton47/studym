#!/usr/bin/env python3
"""
Quick Gmail Setup for Smart Study Platform
Run this script to configure your Gmail credentials
"""

def setup_gmail():
    print("=== Gmail SMTP Setup for Smart Study Platform ===\n")
    
    print("Before proceeding, make sure you have:")
    print("1. ✅ Enabled 2-Factor Authentication on Gmail")
    print("2. ✅ Generated an App Password from Gmail Security settings")
    print("3. ✅ Have your 16-digit App Password ready\n")
    
    proceed = input("Have you completed the above steps? (y/n): ").lower()
    if proceed != 'y':
        print("\n📋 Please complete Gmail setup first:")
        print("1. Go to myaccount.google.com")
        print("2. Security → 2-Step Verification → Enable")
        print("3. Security → App passwords → Generate for Mail")
        print("4. Run this script again")
        return
    
    # Get Gmail credentials
    gmail = input("\n📧 Enter your Gmail address: ").strip()
    if not gmail.endswith('@gmail.com'):
        print("❌ Please enter a valid Gmail address")
        return
    
    app_password = input("🔑 Enter your 16-digit App Password: ").strip().replace(' ', '')
    if len(app_password) != 16:
        print("❌ App Password should be exactly 16 characters")
        return
    
    # Update app.py
    try:
        with open('app.py', 'r') as f:
            content = f.read()
        
        # Replace Gmail credentials
        content = content.replace("EMAIL_ADDRESS = 'your_gmail@gmail.com'", f"EMAIL_ADDRESS = '{gmail}'")
        content = content.replace("EMAIL_PASSWORD = 'your_app_password'", f"EMAIL_PASSWORD = '{app_password}'")
        
        with open('app.py', 'w') as f:
            f.write(content)
        
        print(f"\n✅ Gmail configured successfully!")
        print(f"📧 Gmail: {gmail}")
        print(f"🔑 Password: {'*' * len(app_password)}")
        print(f"\n🚀 You can now send real emails!")
        print(f"💡 Test by: Login → Profile → Add Email → Search Materials → Send Email")
        
    except Exception as e:
        print(f"❌ Error updating configuration: {e}")

if __name__ == "__main__":
    setup_gmail()
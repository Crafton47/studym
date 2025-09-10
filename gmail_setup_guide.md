# Gmail SMTP Setup Guide

## Step 1: Enable 2-Factor Authentication
1. Go to [myaccount.google.com](https://myaccount.google.com)
2. Click "Security" in the left menu
3. Under "Signing in to Google", click "2-Step Verification"
4. Follow the setup process to enable 2FA

## Step 2: Generate App Password
1. In Security settings, click "App passwords"
2. Select "Mail" from the dropdown
3. Click "Generate"
4. Copy the 16-character password (like: `abcd efgh ijkl mnop`)

## Step 3: Update app.py Configuration
Replace these lines in `app.py`:

```python
EMAIL_ADDRESS = 'your_actual_gmail@gmail.com'
EMAIL_PASSWORD = 'your_16_digit_app_password'
```

Example:
```python
EMAIL_ADDRESS = 'john.doe@gmail.com'
EMAIL_PASSWORD = 'abcdefghijklmnop'  # 16 characters, no spaces
```

## Step 4: Test the Setup
1. Update your profile with your Gmail address
2. Search for materials and click "📧 Send to Email"
3. Check your Gmail inbox for the study material

## Troubleshooting

**If emails don't send:**
- Make sure 2FA is enabled
- Use App Password, not regular password
- Check spam/junk folder
- Verify Gmail address is correct
- Ensure no spaces in app password

**Security Notes:**
- Never share your app password
- Don't commit credentials to version control
- Use environment variables in production

## Quick Setup Script
Run this to configure quickly:

```bash
python3 -c "
gmail = input('Enter your Gmail: ')
password = input('Enter App Password: ')
with open('app.py', 'r') as f:
    content = f.read()
content = content.replace('your_gmail@gmail.com', gmail)
content = content.replace('your_app_password', password)
with open('app.py', 'w') as f:
    f.write(content)
print('Gmail configured!')
"
```
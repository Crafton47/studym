# Email API Setup Instructions

## 1. Gmail Setup (Recommended)
- Use your Gmail account or create a new one
- Enable 2-Factor Authentication
- Generate App Password:
  - Go to Google Account settings
  - Security > 2-Step Verification > App passwords
  - Generate password for "Mail"

## 2. Update Configuration
Replace in app.py:
```python
EMAIL_ADDRESS = 'ilovestudy6969@gmail.com'
EMAIL_PASSWORD = 'your_16_digit_app_password'
```

## 3. Alternative Email Providers
For other providers, update SMTP settings:
- **Outlook**: smtp-mail.outlook.com, port 587
- **Yahoo**: smtp.mail.yahoo.com, port 587
- **Custom**: Check your provider's SMTP settings

## 4. Test Setup
- Register with email address
- Search materials and click "Send to Email"
- Check your inbox for the study material

## 5. Security Notes
- Never commit real credentials to code
- Use environment variables in production
- Consider using OAuth2 for better security
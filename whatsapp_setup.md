# WhatsApp API Setup Instructions

## 1. Get Twilio Account
- Sign up at https://www.twilio.com
- Get your Account SID and Auth Token from Console

## 2. WhatsApp Sandbox Setup
- Go to Console > Messaging > Try it out > Send a WhatsApp message
- Follow instructions to join sandbox
- Note the sandbox number: whatsapp:+14155238886

## 3. Update Configuration
Replace in app.py:
```python
TWILIO_ACCOUNT_SID = 'your_actual_account_sid'
TWILIO_AUTH_TOKEN = 'your_actual_auth_token'
```

## 4. Test Setup
- Register with phone number (format: +1234567890)
- Search materials and click "Send to WhatsApp"
- Check your WhatsApp for the message

## 5. Production Setup
For production, you need:
- Verified Twilio phone number
- WhatsApp Business API approval
- Replace sandbox number with your verified number
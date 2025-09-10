# Production Website Setup

## 1. Email Setup for Website

### Gmail Business Setup:
1. Create dedicated Gmail account: `yourwebsite@gmail.com`
2. Enable 2FA and generate App Password
3. Set environment variables on your hosting platform

### Environment Variables:
```bash
EMAIL_ADDRESS=yourwebsite@gmail.com
EMAIL_PASSWORD=your16digitapppassword
FROM_NAME=Your Website Name
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

## 2. Hosting Platforms Setup

### Heroku:
```bash
heroku config:set EMAIL_ADDRESS=yourwebsite@gmail.com
heroku config:set EMAIL_PASSWORD=your16digitapppassword
heroku config:set FROM_NAME="Your Website Name"
```

### Vercel:
Add to vercel.json or dashboard environment variables

### Railway/Render:
Add in dashboard environment variables section

### VPS/Server:
```bash
export EMAIL_ADDRESS=yourwebsite@gmail.com
export EMAIL_PASSWORD=your16digitapppassword
```

## 3. Alternative Email Providers

### SendGrid (Recommended for high volume):
```python
SMTP_SERVER=smtp.sendgrid.net
SMTP_PORT=587
EMAIL_ADDRESS=apikey
EMAIL_PASSWORD=your_sendgrid_api_key
```

### Mailgun:
```python
SMTP_SERVER=smtp.mailgun.org
SMTP_PORT=587
EMAIL_ADDRESS=your_mailgun_email
EMAIL_PASSWORD=your_mailgun_password
```

## 4. Production Checklist

- [ ] Set up dedicated email account
- [ ] Configure environment variables
- [ ] Test email sending
- [ ] Set up SSL certificate
- [ ] Configure domain
- [ ] Set up database backup
- [ ] Monitor email delivery

## 5. Security Best Practices

- Never commit credentials to code
- Use environment variables
- Enable 2FA on email account
- Monitor email usage
- Set up email rate limiting
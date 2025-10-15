# ============================================================================
# 23. EMAIL & SMS AUTOMATION
# ============================================================================
# WHAT: Send automated emails and SMS messages using Python
# WHY: Notifications, alerts, reports, reminders - automate communication
# WHEN: Daily reports, error alerts, customer notifications, reminders
# NOTE: Email uses smtplib (built-in), SMS needs Twilio (pip install twilio)

print("="*60)
print("EMAIL & SMS AUTOMATION")
print("="*60)

# ============================================================================
# EMAIL AUTOMATION (SMTPLIB)
# ============================================================================

print("\n" + "="*60)
print("EMAIL AUTOMATION - SMTPLIB")
print("="*60)

print("""
💡 Why Automate Emails?
- Send daily/weekly reports to stakeholders
- Alert notifications (errors, thresholds)
- Customer follow-ups
- Scheduled reminders
- Batch email campaigns

smtplib is built-in Python (no installation needed)
""")

# ============================================================================
# BASIC EMAIL SENDING
# ============================================================================

print("\n1. BASIC EMAIL EXAMPLE:")
print("""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "your-email@gmail.com"
sender_password = "your-app-password"  # Use App Password, not regular password!
receiver_email = "recipient@example.com"

# Create message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = "Automated Report"

# Email body
body = \"\"\"
Hello,

This is an automated email from Python.

Best regards,
Your Automation System
\"\"\"
msg.attach(MIMEText(body, 'plain'))

# Send email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable security
    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    print("✓ Email sent successfully!")
except Exception as e:
    print(f"✗ Error sending email: {e}")
""")

# ============================================================================
# HTML EMAILS
# ============================================================================

print("\n2. HTML EMAILS (FORMATTED):")
print("""
from email.mime.text import MIMEText

# HTML email body
html_body = \"\"\"
<html>
  <body>
    <h2>Daily Sales Report</h2>
    <p>Total Revenue: <strong>$5,432</strong></p>
    <table border="1">
      <tr><th>Product</th><th>Sales</th></tr>
      <tr><td>Product A</td><td>$2,000</td></tr>
      <tr><td>Product B</td><td>$3,432</td></tr>
    </table>
  </body>
</html>
\"\"\"

msg.attach(MIMEText(html_body, 'html'))
""")

# ============================================================================
# EMAIL WITH ATTACHMENTS
# ============================================================================

print("\n3. EMAIL WITH ATTACHMENTS:")
print("""
from email.mime.base import MIMEBase
from email import encoders
import os

# Attach file
filename = "report.pdf"
with open(filename, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

msg.attach(part)

# Send with attachment
server.send_message(msg)
print(f"✓ Email sent with attachment: {filename}")
""")

# ============================================================================
# COMMON EMAIL PROVIDERS
# ============================================================================

print("\n" + "="*60)
print("SMTP SETTINGS FOR COMMON PROVIDERS")
print("="*60)

print("""
Gmail:
  Server: smtp.gmail.com
  Port: 587 (TLS) or 465 (SSL)
  Note: Use App Password (not regular password)
  Enable: https://myaccount.google.com/apppasswords

Outlook/Hotmail:
  Server: smtp-mail.outlook.com
  Port: 587

Yahoo:
  Server: smtp.mail.yahoo.com
  Port: 587

Office 365:
  Server: smtp.office365.com
  Port: 587

⚠️ Security Best Practices:
- NEVER hardcode passwords in scripts
- Use environment variables: os.getenv("EMAIL_PASSWORD")
- Use App Passwords, not main password
- Store credentials in .env file (not in git)
- Encrypt sensitive data
""")

# ============================================================================
# SMS AUTOMATION (TWILIO)
# ============================================================================

print("\n" + "="*60)
print("SMS AUTOMATION - TWILIO")
print("="*60)

print("""
💡 Why Automate SMS?
- Critical alerts (server down, errors)
- Two-factor authentication (2FA)
- Order confirmations
- Appointment reminders
- Emergency notifications

Install: pip install twilio
Sign up: https://www.twilio.com (free trial available)
""")

print("\n1. BASIC SMS EXAMPLE:")
print("""
from twilio.rest import Client

# Twilio credentials (from dashboard)
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = '+1234567890'  # Your Twilio number
recipient_number = '+0987654321'

# Create client
client = Client(account_sid, auth_token)

# Send SMS
message = client.messages.create(
    body="Alert: Server CPU usage above 90%!",
    from_=twilio_number,
    to=recipient_number
)

print(f"✓ SMS sent! Message SID: {message.sid}")
""")

print("\n2. SMS WITH STATUS TRACKING:")
print("""
# Send and track
message = client.messages.create(
    body="Your order #1234 has been shipped!",
    from_=twilio_number,
    to=recipient_number
)

# Check status
print(f"Message Status: {message.status}")
print(f"Message SID: {message.sid}")

# Possible statuses: queued, sending, sent, delivered, failed
""")

# ============================================================================
# PRACTICAL AUTOMATION IDEAS
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL AUTOMATION IDEAS (FROM ATBS)")
print("="*60)

print("""
💡 Email Automation Use Cases:

1. Daily Report Emailer
   - Fetch data from database/API
   - Generate report (CSV/Excel)
   - Email to stakeholders at 9am

2. Error Alert System
   - Monitor logs/metrics
   - Email when threshold exceeded
   - Include error details + timestamp

3. Invoice Sender
   - Generate invoices automatically
   - Attach PDF to email
   - Send to customers

4. Reminder System
   - Check calendar/database
   - Send reminder emails
   - Scheduled follow-ups

5. Newsletter Automation
   - Pull latest articles
   - Format as HTML email
   - Send to subscriber list

💡 SMS Automation Use Cases:

1. Server Monitoring
   - Alert when server down
   - CPU/Memory threshold alerts
   - Database connection errors

2. Form Submission Alerts
   - New customer inquiry
   - High-value orders
   - Critical issues reported

3. 2FA/OTP Codes
   - Generate verification codes
   - Send via SMS
   - Time-limited authentication

4. Delivery Notifications
   - Order shipped alerts
   - Delivery confirmations
   - Status updates
""")

# ============================================================================
# COMPLETE EXAMPLE: DAILY REPORT
# ============================================================================

print("\n" + "="*60)
print("COMPLETE EXAMPLE: DAILY REPORT EMAILER")
print("="*60)

print("""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
import csv

def send_daily_report():
    # 1. Generate report data
    report_data = [
        ["Product", "Sales", "Revenue"],
        ["Product A", 45, "$2,250"],
        ["Product B", 67, "$3,350"],
        ["Product C", 23, "$1,150"]
    ]

    # 2. Save to CSV
    filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(report_data)

    # 3. Create email
    msg = MIMEMultipart()
    msg['From'] = os.getenv("SENDER_EMAIL")
    msg['To'] = "manager@company.com"
    msg['Subject'] = f"Daily Sales Report - {datetime.now().strftime('%Y-%m-%d')}"

    body = f\"\"\"
    Hi Team,

    Please find attached the daily sales report for {datetime.now().strftime('%Y-%m-%d')}.

    Summary:
    - Total Products Sold: 135
    - Total Revenue: $6,750

    Best regards,
    Automated Reporting System
    \"\"\"

    msg.attach(MIMEText(body, 'plain'))

    # 4. Attach CSV
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(part)

    # 5. Send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv("SENDER_EMAIL"), os.getenv("EMAIL_PASSWORD"))
        server.send_message(msg)
        server.quit()
        print(f"✓ Daily report sent: {filename}")
    except Exception as e:
        print(f"✗ Error: {e}")
        # Optional: Send SMS alert about email failure
        # send_sms_alert(f"Email report failed: {e}")

    # 6. Cleanup
    os.remove(filename)

# Schedule this function to run daily at 9am
# Use: schedule library or cron job
""")

# ============================================================================
# INTEGRATION WITH WORKFLOWS
# ============================================================================

print("\n" + "="*60)
print("INTEGRATION WITH BI/AUTOMATION WORKFLOWS")
print("="*60)

print("""
🔗 Email/SMS in Data Pipelines:

1. ETL Pipeline Notifications
   - Extract: Data loaded successfully → Email confirmation
   - Transform: Errors found → SMS alert to engineer
   - Load: Report ready → Email with Power BI link

2. Make.com / n8n Integration
   - Trigger: Scheduled (daily 9am)
   - Action 1: Python script generates report
   - Action 2: Send email via Gmail node
   - Action 3: Send SMS via Twilio node
   - Fallback: If email fails, send SMS

3. AI/LLM Workflows
   - AI generates summary → Email to stakeholders
   - LLM finds anomalies → SMS critical alerts
   - Automated responses → Email replies

4. Monitoring & Alerts
   - Power BI refresh fails → Email + SMS
   - API rate limit reached → Notification
   - Database backup complete → Confirmation

💡 Best Practice Stack:
   - Email: Regular reports, detailed info, attachments
   - SMS: Critical alerts, urgent notifications only
   - Slack/Teams: Team collaboration updates
   - Choose based on urgency and detail level
""")

# ============================================================================
# SECURITY & COMPLIANCE
# ============================================================================

print("\n" + "="*60)
print("SECURITY & COMPLIANCE")
print("="*60)

print("""
⚠️ Important Considerations:

1. Email Security
   - Use TLS/SSL encryption (always)
   - Store credentials in environment variables
   - Use OAuth2 for Gmail (preferred over app passwords)
   - Never commit passwords to git

2. SMS Compliance (GDPR, TCPA)
   - Get explicit consent before sending
   - Include opt-out mechanism
   - Don't send marketing via SMS without permission
   - Log consent and opt-outs

3. Rate Limiting
   - Email: Don't spam, use bulk email services for campaigns
   - SMS: Twilio has rate limits, monitor usage
   - Implement delays between messages

4. Error Handling
   - Catch exceptions (network errors, auth failures)
   - Retry logic for transient errors
   - Fallback communication methods
   - Log all send attempts

5. Data Privacy
   - Don't include sensitive data in SMS
   - Encrypt email attachments if needed
   - Anonymize personal information
   - Follow GDPR/privacy laws

Example: Secure Credential Management
------
# .env file (not in git)
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
TWILIO_SID=your-sid
TWILIO_TOKEN=your-token

# Python script
import os
from dotenv import load_dotenv

load_dotenv()
email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASS")
""")

print("\n✓ Email & SMS automation concepts covered!")
print("\n📦 Required packages:")
print("  - Email: smtplib (built-in)")
print("  - SMS: pip install twilio")
print("  - Credentials: pip install python-dotenv")

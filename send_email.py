import smtplib
from email.message import EmailMessage
from datetime import date

# ---- CONFIGURATION ----
SENDER_EMAIL = "jrlope3z42@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use app-specific password if using Gmail
RECIPIENT_EMAIL = "recipient@example.com"
SUBJECT = f"🗞 Daily News Summary - {date.today()}"

# ---- SEND EMAIL FUNCTION ----
def send_news_email(summaries):
    msg = EmailMessage()
    msg["Subject"] = SUBJECT
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL

    # Create email body from list of summaries
    body = "\n\n".join([f"📌 Summary {i+1}:\n{summary}" for i, summary in enumerate(summaries)])
    msg.set_content(body)

    # Send email using Gmail SMTP server
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("✅ Email sent successfully.")
    except Exception as e:
        print("❌ Failed to send email:", str(e))

# send_email.py
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_youtube_idea():
    """
    Function to read the content from "Youtube_idea.txt" file.
    """
    with open(os.path.join("data", "Youtube_idea.txt"), "r", encoding="utf-8") as file:
        youtube_idea = file.read()
    return youtube_idea

def read_ai_news():
    """
    Function to read the content from "AI_news.txt" file.
    """
    with open(os.path.join("data", "AI_news.txt"), "r", encoding="utf-8") as file:
        ai_news = file.read()
    return ai_news

def send_email_with_attachments(subject, recipient_email, youtube_idea, ai_news):
    """
    Function to send the email with "Youtube_idea.txt" and "AI_news.txt" as attachments.
    """
    # Set up the email content
    message = MIMEMultipart()
    message["From"] = "your_email@example.com"
    message["To"] = recipient_email
    message["Subject"] = subject

    # Attach "Youtube_idea.txt"
    youtube_idea_attachment = MIMEText(youtube_idea)
    youtube_idea_attachment.add_header("Content-Disposition", "attachment", filename="Youtube_idea.txt")
    message.attach(youtube_idea_attachment)

    # Attach "AI_news.txt"
    ai_news_attachment = MIMEText(ai_news)
    ai_news_attachment.add_header("Content-Disposition", "attachment", filename="AI_news.txt")
    message.attach(ai_news_attachment)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_email_password")
        server.sendmail("your_email@example.com", recipient_email, message.as_string())

def send_email(subject, recipient_email, youtube_content, ai_news_content):
    """
    Function to send an email with the generated content.

    Args:
        subject (str): The subject of the email.
        recipient_email (str): The email address of the recipient.
        youtube_content (str): The content related to YouTube ideas.
        ai_news_content (str): The content related to AI news.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    # Email configuration
    sender_email = "your_email@example.com"  # Replace with your sender email address
    smtp_server = "smtp.example.com"  # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP port
    smtp_username = "your_username"  # Replace with your SMTP username
    smtp_password = "your_password"  # Replace with your SMTP password

    # Create a MIMEText object for the email content
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Attach the content for YouTube ideas and AI news to the email
    message.attach(MIMEText(youtube_content, "plain"))
    message.attach(MIMEText(ai_news_content, "plain"))

    try:
        # Establish a connection with the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to the SMTP server
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

        # Close the SMTP connection
        server.quit()

        print("Email sent successfully.")
        return True
    except Exception as e:
        print("Failed to send the email:", e)
        return False

if __name__ == "__main__":
    try:
        print("Send Email: Sending email with content...")
        youtube_idea = read_youtube_idea()
        ai_news = read_ai_news()

        # Customize the email subject and recipient email address here.
        subject = "AI System Content"
        recipient_email = "recipient@example.com"

        send_email_with_attachments(subject, recipient_email, youtube_idea, ai_news)

        # Alternatively, you can use the send_email function for sending email without attachments
        # send_email(subject, recipient_email, youtube_idea, ai_news)

        print("Send Email: Email sent successfully.")
    except Exception as e:
        print("Send Email: An error occurred while sending the email:", e)

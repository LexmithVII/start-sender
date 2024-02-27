Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import smtplib
... from email.mime.multipart import MIMEMultipart
... from email.mime.text import MIMEText
... import time
... 
... def send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body):
...     try:
...         # Set up the SMTP server and log in
...         server = smtplib.SMTP_SSL(smtp_server, port)
...         server.login(sender_email, sender_password)
... 
...         # Create the email
...         email = MIMEMultipart()
...         email['From'] = sender_email
...         email['To'] = recipient_email
...         email['Subject'] = subject
...         email.attach(MIMEText(body, 'html', _charset='UTF-8'))  # Changed 'plain' to 'html' and added UTF-8 charset
... 
...         # Send the email
...         server.send_message(email)
...         server.quit()
...         print("Email sent successfully!")
...     except Exception as e:
...         print(f"Failed to send email: {str(e)}")
... 
... # Request SMTP details
... smtp_server = input("Enter your SMTP server: ")
... port = int(input("Enter your SMTP server port: "))
... sender_email = input("Enter your email: ")
... sender_password = input("Enter your email password: ")
... 
... # Request email details
... recipient_email = input("Enter the recipient's email: ")
... subject = input("Enter the email subject: ")
... body = input("Enter the email body: ")
... 
... # Send the email
... user_input = input("Enter 'send' to start sending: ")
... if user_input.lower() == 'send':
...     send_email(smtp_server, port, sender_email, sender_password, recipient_email, subject, body)
    print("Email sent!")

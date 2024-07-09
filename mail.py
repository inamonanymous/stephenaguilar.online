import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

root_email = 'youremail@yourdomain.com'
email_password = '15digitpassword'
def establish_smtp_connection():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(root_email, email_password)
    return server

def sendMessage(name:str, user_email:str, user_message:str):
    server = establish_smtp_connection()
    if not is_valid_email(user_email):
        server.quit()
        return False
    message = MIMEMultipart()
    message["From"] = root_email
    message["To"] = user_email
    message["Subject"] = "Thank you for Reaching me Out!🎉"
    body_message = f"""
                    Hi {name},

                    Thank you for getting in touch through my portfolio website. I appreciate you taking the time to reach out, and I'm excited to connect with you.

                    I noticed that you mentioned "{user_message}". I'd love to discuss it further and see how I can assist you with that.

                    Could we schedule a time to chat? Please let me know your availability, and we can set up a meeting that works for both of us.

                    Looking forward to speaking with you soon!

                    Best regards,
                    Stephen Joaquin G. Aguilar

                    📞: (63+) 956 064 6626
                    🌐: https://www.facebook.com/stephen.joaquin.52
                    🌐: https://www.instagram.com/stephen_420__
                    🌐: http://www.stephenaguilar.online
                    """
                    
    message.attach(MIMEText(body_message, "plain"))
    server.send_message(message)
    server.quit()
    return True

def sendMessageSelf(user_name, user_email, user_phone, user_message):
    server = establish_smtp_connection()
    if not is_valid_email(user_email):
        server.quit()
        return False
    message = MIMEMultipart()
    message["From"] = root_email
    message["To"] = root_email
    message["Subject"] = "Someone reached you out!🎉"
    body_message = f"""
                    Name: {user_name}
                    Email Address: {user_email}
                    Phone Number: {user_phone}
                    Message: {user_message}
                    """      
    message.attach(MIMEText(body_message, "plain"))
    server.send_message(message)
    server.quit()
    return True

def is_valid_email(email):
    # Define a regular expression for validating an Email
    email_regex = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    # Match the email with the regex
    return re.match(email_regex, email) is not None
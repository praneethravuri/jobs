import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

smtp_port = 587                
smtp_server = "smtp.gmail.com"  

email_from = "pravdev10@gmail.com"
company_name = "ServiceNow"

email_list = [
    {"name" : "name@gmail.com"},
    {"name2" : "name2@gmail.com"}
]


password = os.getenv("GMAIL_APP_PASSWORD")

def send_emails(email_list):
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls()
    TIE_server.login(email_from, password)
    print("Successfully connected to server")
    print()

    for person in email_list:
        first_name = person["name"].split()[0]
        person_email = person["email"]
        body = f"""
        Hello {first_name},

        I noticed that you are working at {company_name}. I'm a CS grad from GMU looking for new opportunities and wonder if you could refer me to various positions at {company_name}.
        
        The Job IDs:
        
        1. Technical Support Engineer - JB0044741
        2. Software Engineer - JB0044400
        3. Software Engineer - JB0045871
        
        Thank you,
        Praneeth Ravuri
        Ph: +1 571-622-8648
        LinkedIn: https://www.linkedin.com/in/prav25/
        Website: https://praneethravuri.com/
        GitHub: https://github.com/praneethravuri
        
        """

        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = person_email
        msg['Subject'] = f"Looking for opportunities at {company_name}"

        msg.attach(MIMEText(body, 'plain'))

        text = msg.as_string()

        print(f"Sending email to: {person['name']}...")
        TIE_server.sendmail(email_from, person_email, text)
        print(f"Email sent to: {person['name']}")
        print()

    TIE_server.quit()
    print("Disconnected from server.")

send_emails(email_list)

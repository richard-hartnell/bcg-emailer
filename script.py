import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# you don't need to point to the meeting I guess

meeting_date = "Sunday, January 43rd" # prompt('What is the date of the meeting?')

# write the reminder email for 1 week

week_reminder = '''
Hi all,

Here's the week-ahead reminder of our next Circus Guild meeting on ${date}.

Per usual, if you have any agenda items to add you can do so in the description field of the Google Calendar event. If you don't want a proposal subject to a ten-day waiting period presuming it passes this Sunday, then please submit it to the group in writing by this upcoming Thursday.

Also per usual, if you need to attend the event virtually just let us know.

RH
'''

# write the reminder email for 3 days

days_reminder = '''
Dear BCG,

Here is your additional reminder for the upcoming Guild meeting on ${meeting_date} at 5 PM.

If you intend to pass any proposals without a ten-day waiting period, please submit them to the Guild by writing by end of day today.
'''

# email to bcg

# Your email and password
email_address = "richard@bellinghamcircusguild.com"
with open('email_password.txt', 'r') as file:
    email_password = file.read().strip()

# Email setup
def send_email(recipient_email, subject, body):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to the Dreamhost SMTP server
        with smtplib.SMTP_SSL('smtp.dreamhost.com', 465) as server:
            server.login(email_address, email_password)
            # Send the email
            server.sendmail(email_address, recipient_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
send_email("rfreemanh@gmail.com", "Test Subject", week_reminder)
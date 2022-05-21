import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "roytestingpython@gmail.com"
receiver_email = "roychongzhenrong@gmail.com"
password = input("Type your password and press enter:")

#Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "multipart test"
msg["From"] = sender_email
msg["To"] = receiver_email
filename = "document.pdf"

#HTML Message Part
html = """\
<html>
  <body>
    <p><b>Python Mail Test</b>
    <br>
       This is HTML email with attachment.<br>
       Click on <img src="https://pastepixel.com/image/kDChwT3Pas7BfDvgeYuv.png" alt=""/>
       for more python articles.
    </p>
  </body>
</html>
"""

part = MIMEText(html, "html")
msg.attach(part)


# Set mail headers
part.add_header(
    "Content-Disposition",
    "attachment", filename= filename
)
msg.attach(part)

# Create secure SMTP connection and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )
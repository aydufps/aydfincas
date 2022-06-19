import smtplib
import string

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def smtp_gmail():
    username = "jefersonurielhc@ufps.edu.co"
    password = "mjsytbqwyfgsgzdg"
    smtp_server = "smtp.gmail.com:587"
    email_from = "jefersonurielhc@ufps.edu.co"
    email_to = "asimplemailmore@gmail.com"
    email_body = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
    <head></head>
    <body>
        <p>Hi!<br>
        How are you?<br>
        Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')
    s.attach(part1)
    s.attach(part2)
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(username, email_to, s.as_string())
    s.quit()


smtp_gmail()

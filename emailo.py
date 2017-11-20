#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scifi_finder import find_movies_with_genre
import codecs


newsletter_html_with_content = find_movies_with_genre('Your_API_Key', 878)

sender = "youremail@gmail.com"
recipient = "subscriber@gmail.com, othersubscriber@live.it"

# Create message container
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = sender
msg['To'] = recipient

# Create body of the message (a plain-text and an HTML version).
msg_text = "Hi!\nHow are you?\nHere are the movies: __"
msg_html = newsletter_html_with_content

# Record the MIME types of both parts
part1 = MIMEText(msg_text, 'plain')
part2 = MIMEText(msg_html.encode('utf-8'), 'html')

# Attach parts into message container.
msg.attach(part1)
msg.attach(part2)

# Sends the newsletter via gmail server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("youremail@gmail.com", "YourPassword!")


try:
    server.sendmail(sender, recipient, msg.as_string())
    print "Email sent!"
    print newsletter_html_with_content
except:
    print "Not working, son"

from flask import Flask
import email
import imaplib
import asyncio
import time
from creds import username
from creds import password
from creds import imap_server

mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)

app = Flask(__name__)
@app.route('/')
def index():
    while(True):
        time.sleep(10)

        try:
            # select unread emails
            mail.select("inbox")
            result, data = mail.uid('search', None, "UNSEEN")
            inbox_item_list = data[0].split()

            # if there are unread emails, parse them
            if(len(inbox_item_list) > 0):

                # decode formatting
                for item in inbox_item_list:
                    result2, email_data = mail.uid('fetch', item, '(RFC822)')
                    raw_email = email_data[0][1].decode("utf-8")
                    email_message = email.message_from_string(raw_email)

                    # find emails
                    counter = 1
                    for part in email_message.walk():
                        if part.get_content_maintype() == "multipart":
                            continue
                        filename = part.get_filename()
                        if not filename:
                            ext = '.html'
                            filename = 'msg-part-%08d%s' %(counter, ext)
                        counter += 1
                        content_type = part.get_content_type()

                        # check for uw alert
                        payload = part.get_payload()
                        if "plain" in content_type and "alert.uw.edu" in payload:
                            return(payload)

                # if no unread emails, continue loop
                else:
                    continue
        except:
            mail.login(username, password)
            continue

if __name__ == '__main__':
    app.run()

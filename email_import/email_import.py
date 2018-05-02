import email
import imaplib
import asyncio
import time
from creds import username
from creds import password

while(True):
    time.sleep(60)
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)

    mail.select("inbox")

    result, data = mail.uid('search', None, "UNSEEN")
    # print(data)
    inbox_item_list = data[0].split()
    # print(len(inbox_item_list))
    # print(type(len(inbox_item_list)))

    # if there are unread emails, parse them
    if(len(inbox_item_list) > 0):
        most_recent = inbox_item_list[-1]
        oldest = inbox_item_list[0]

        for item in inbox_item_list:
            result2, email_data = mail.uid('fetch', item, '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_message = email.message_from_string(raw_email)

            subject = email_message['Subject']
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

                # filename
                payload = part.get_payload()
                if "plain" in content_type and "alert.uw.edu" in payload:
                    print(part.get_payload())
        # if no unread emails, continue loop
        else:
            continue

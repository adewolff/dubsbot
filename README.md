# Dubsbot [![Python 3](https://pyup.io/repos/github/adewolff/dubsbot/python-3-shield.svg)](https://pyup.io/repos/github/adewolff/dubsbot/)

## What is it?

Dubsbot will scan an email account for UW alerts, and post them to a specified Discord channel.

## How do I use it?

- Create `setup.py`
  - Declare `botkey` with your Discord bot key
  - Declare `channelid` with the channel id you want Dubsbot to post alerts to

- Inside the email_import folder create `creds.py`
  - Declare `imap_server` with the url for the imap server you want to use (e.g."imap.gmail.com")
  - Declare `username` with the username for the email account
  - Declare `password` with the password for the account

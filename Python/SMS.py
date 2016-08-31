#!/usr/bin/env python

import sys
from twilio.rest import TwilioRestClient

# Credentials from your Twilio account. 
account_sid = "AC7815906e65584b94c2441a98bd972816"
auth_token  = "00f993371dd76de8357d015bdcc3a666"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
	body="Hello, SMS!",
	to="+13852013345", # Your phone number.
	from_="+18329813339" # Your Twilio number.
) 

# Sends the message via SMS and prints some sort of message id to stdout.
print message.sid

sys.exit()


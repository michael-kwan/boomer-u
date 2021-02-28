# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import json
import random

a = open('auth.json')
auth = json.load(a)


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = auth['TWILIO_ACCOUNT_SID']
auth_token = auth['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


#get list of numbers

numbers = open("nums.json")
nums = json.load(numbers)

#get list of things to send

msgs = open("msgs.json")
messages = json.load(msgs)

rnum = random.randrange(0, len(messages['words']))

word = messages['words'][rnum]['word'].upper()
definition = messages['words'][rnum]['definition']

msg_body = "Hello from Boomer University! \n\n"\
"The word of the day is {}, which means: \n\n"\
"{}".format(word, definition)


for n in nums['nums']:
    print(n)
    message = client.messages \
                    .create(
                         body=msg_body,
                         from_='+12168687855',
                         to=n['number']
                    )

print(message.sid)

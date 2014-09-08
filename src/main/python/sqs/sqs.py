__author__ = 'mhoyer'

import boto.sqs
from boto.sqs.message import Message

sqs = boto.sqs.connect_to_region("eu-west-1")

testqueue = sqs.create_queue('testqueue')

# write message
message = Message()
message.set_body("My first test message")
testqueue.write(message)


# read message
messages = testqueue.get_messages()
print messages[0].get_body()

sqs.delete_queue(testqueue)
from quassel import *

def onMessageRecieved(bot, message):
    if message['type'] == Message.Type.Plain or message['type'] == Message.Type.Action:
        messageFormat = '{:<16}\t{:>16}: {}'
        output = messageFormat.format(*[
            message['bufferInfo']['name'],
            message['sender'].split('!')[0],
            message['content'],
        ])
        print(output)
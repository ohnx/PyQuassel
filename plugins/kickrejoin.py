from quassel import *
import json

def onMessageRecieved(bot, message):
    if message['type'] == Message.Type.Kick:
        if message['content'].split(' ')[0] in bot.config.nicks:
            if message['bufferInfo']['name'] in bot.config.kickrejoinChannels:
                bot.sendInput(message['bufferInfo']['id'], "/JOIN " + message['bufferInfo']['name'])

from quassel import *
import pickle
import markovify
import os

MARKOV_SOURCE = 'plugins/markov/source.markov'

markov_chain = None

def onSessionStarted(bot):
    global MARKOV_SOURCE
    global markov_chain

    if os.path.exists(MARKOV_SOURCE):
        # already exists
        print('Opening existing markov chain')
        markov_chain = pickle.load(open(MARKOV_SOURCE, 'rb'))
    else:
        # need to generate
        print('Generating markov chain...')
        with open('plugins/markov/source.txt') as f:
            text = f.read()
        markov_chain = markovify.NewlineText(text)
        pickle.dump(markov_chain, open(MARKOV_SOURCE, 'wb'))
    print('Loaded successfully!')

def onMessageRecieved(bot, message):
    if message['type'] == Message.Type.Plain or message['type'] == Message.Type.Action:
        if message['bufferInfo']['name'] in bot.config.markovChanels and bot.config.markovPings[0] in message['content']:
            sender = message['sender'].split('!')[0]
            if not (sender in bot.config.markovIgnore):
                msg = markov_chain.make_short_sentence(140)
                bot.sendInput(message['bufferInfo']['id'], sender + ': ' + msg)

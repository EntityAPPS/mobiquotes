from atproto import Client
import random

client = Client()
client.login('<username>.bsky.social', '<password>')

lines = open('quotes.txt').read().splitlines()
myline =random.choice(lines)

post = client.send_post(myline)
from slacker import Slacker
from decouple import config
import websocket
from pprint import pprint
import json


TOKEN = config("API_TOKEN")
slack = Slacker(TOKEN)
response = slack.rtm.start()
meta = response.body

ws = websocket.create_connection(meta['url'])

try:
    while True:
        response = json.loads(ws.recv())
        if 'message' == response.get('type', None):
            if 'channel' in response:
                ws.send(json.dumps({
                    'channel': response['channel'],
                    'type': 'message',
                    'text': 'Echo: ' + response['text'],
                }))
except KeyboardInterrupt:
    pass
finally:
    ws.close()

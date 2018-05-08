import json
from slacker import Slacker
import websocket


class BotBase:
    def __init__(self, token):
        response = Slacker(token).rtm.start()
        meta = response.body
        self.ws = websocket.create_connection(meta['url'])

    def recv(self):
        return json.loads(self.ws.recv())

    def send(self, obj, opcode=websocket.ABNF.OPCODE_TEXT):
        try:
            payload = json.dumps(obj)
        except TypeError:
            payload = obj

        return self.ws.send(payload, opcode)

    def close(self):
        self.ws.close()

    def don_hello(self):
        pass

    def on_message(self, channel, **kwargs):
        user = kwargs.pop('user', '')
        text = kwargs.pop('text', '')

        if user and text and text.startswith('!'):
            cmd = text[1:]
            query = ""
            fn_name = 'cmd_' + cmd
            fn = getattr(self, fn_name, None)
            if callable(fn):
                fn(channel, user, query)
            else:
                self.post_message(channel, "지원하지 않는 명령어 입니다.")

    def post_message(self, channel, text):
        self.send({
            'channel': channel,
            'type': 'message',
            'text': text
        })

    def run_forever(self):
        try:
            while True:
                response = self.recv()
                # print(response)
                if 'type' in response:
                    fn_name = 'on_' + response.pop('type')
                    fn = getattr(self, fn_name, None)
                    if callable(fn):
                        fn(**response)
        except KeyboardInterrupt:
            pass
        finally:
            self.close()

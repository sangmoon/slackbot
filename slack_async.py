import asyncio
import json
from slacker import Slacker
import websockets
from decouple import config


async def bot(token):
    response = Slacker(token).rtm.start()
    meta = response.body

    # 현 Slack Team 에 대한 다양한 정보
    ws = await websockets.connect(meta['url'])
    try:
        while True:
            response = json.loads(await ws.recv())
            if 'message' == response.get('type', None):
                if 'channel' in response:
                    await ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': 'Echo : ' + response['text'],
                    }))
    finally:
        await ws.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    TOKEN = config("API_TOKEN")
    try:
        loop.run_until_complete(bot(TOKEN))
        # bot() 코루틴이 종료될 때까지, 블록킹 상태
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()

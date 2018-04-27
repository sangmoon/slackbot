from slacker import Slacker
from decouple import config
import websocket
from pprint import pprint
import json
import random


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
                if "!명령어" == response['text']:
                    ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': '`!명령어`/`준연`/`갓`/`!정보`/`!봇`/`SAS랜덤`',
                    }))
                elif "준연" in response['text'] or "갓" in response['text']:
                    ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': '`갓준연` ㅇㅈ하는 각? ㅇ ㅇㅈ :thumbsup_all:',
                    }))

                elif response['text'].startswith('!정보'):
                    ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': '''레드마인 : http://192.168.2.185:2222/ \n 소프트 세미나: http://192.168.15.58/mediawiki/index.php/SoftPM/Soft_%EC%84%B8%EB%AF%B8%EB%82%98  \n 클라우드실 교육자료 : http://192.168.2.185:2222/projects/temp/wiki/%EC%97%B0%EA%B5%AC%EC%86%8C_%EA%B3%B5%ED%86%B5_%EA%B5%90%EC%9C%A1_%EB%B0%8F_%EC%BB%A4%EB%A6%AC%ED%81%98%EB%9F%BC \n PAS실 자료 http://192.168.2.175:10080/cloud3/ProObjectPlus/wikis/home''',
                    }))
                elif "!봇" == response['text']:
                    ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': '''
                                `SAS팀` 봇입니다. 기능 추가/버그 제보 환영합니다.`email`: sangmoon_park@tmax.co.kr
                                ''',
                    }))

                elif "SAS랜덤" in response['text']:
                    lst = ['상문', '준연', '성수', '종호', '희수', '상준',
                           '도은', '지원', '민희', '유나']
                    num_of_select = 2
                    random_lst = random.sample(lst, num_of_select)
                    ws.send(json.dumps({
                        'channel': response['channel'],
                        'type': 'message',
                        'text': random_lst[0] + " or/and " + random_lst[1],
                    }))
                # else:
                #     ws.send(json.dumps({
                #         'channel': response['channel'],
                #         'type': 'message',
                #         'text': 'Echo: ' + response['text'],
                #     }))
except KeyboardInterrupt:
    pass
finally:
    ws.close()

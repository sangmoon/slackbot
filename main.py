import json
import requests
import random
from decouple import config
from bot import BotBase


class Bot(BotBase):
    def cmd_명령어(self, channel, user, query):
        message = '`!명령어`/`!정보`/`!봇`/`!sas랜덤`'
        self.post_message(channel,  message)

    def cmd_정보(self, channel, user, query):
        message = '''
레드마인: http://192.168.2.185:2222/\n
소프트 PM팀: http://192.168.13.80/mediawiki/index.php/Main_Page\n
클라우드실 교육자료 : http://192.168.2.185:2222/projects/temp/wiki/%EC%97%B0%EA%B5%AC%EC%86%8C_%EA%B3%B5%ED%86%B5_%EA%B5%90%EC%9C%A1_%EB%B0%8F_%EC%BB%A4%EB%A6%AC%ED%81%98%EB%9F%BC\n
PAS실 자료 http://192.168.2.175:10080/cloud3/ProObjectPlus/wikis/home\n
PO manager 서버: http://192.168.15.70:8080/promanager'''
        self.post_message(channel, message)

    def cmd_봇(self, channel, user, query):
        message = "`SAS팀` 봇입니다. 기능 추가/버그 제보 환영합니다.`email`: sangmoon_park@tmax.co.kr"
        self.post_message(channel, message)

    def cmd_sas랜덤(self, channel, user, query):
        lst = ['상문', '준연', '성수', '종호', '희수', '상준',
                           '도은', '지원', '민희', '유나']
        num_of_select = 2
        random_lst = random.sample(lst, num_of_select)
        message = random_lst[0] + " or/and " + random_lst[1]
        self.post_message(channel, message)


if __name__ == '__main__':
    TOKEN = config("API_TOKEN")
    Bot(TOKEN).run_forever()

from slacker import Slacker
from decouple import config

API_TOKEN = config("API_TOKEN")
slack = Slacker(API_TOKEN)

slack.chat.post_message("#slackbot_test", "test message")

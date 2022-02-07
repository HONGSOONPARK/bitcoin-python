import datetime
import telegram
import logging

# 텔레그램 토큰
# 머리돌
stonehead_token = "1635387024:AAEQfnk-F5A274EmpY1SSFY8bPYJbdULf2g"

# 모아이대가리
moaihead_token = "5272244147:AAHpcSWzIapXCNlm7yxW7Xvqs2hLRhU5UGs"

# stoneheadcoding , @daegalibot
# 머리돌 채널 ID  : -1001280712219
stonehead_channel = "-1001280712219"

# 모아이 채널 ID : -1001318811692
moaihead_channel = "-1001318811692"

moaihead_bot = telegram.Bot(token=moaihead_token)

stonehead_bot = telegram.Bot(token=stonehead_token)

# 텔레그램 채널에 메세지 보내기


def stonehead_channel_send_msg(msg):
    logging.info("send msg")
    stonehead_bot.sendMessage(chat_id=stonehead_channel, text=msg)


def moaihead_channel_send_msg(msg):
    logging.info("send msg")
    moaihead_bot.sendMessage(chat_id=moaihead_channel, text=msg)

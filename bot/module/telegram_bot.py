import datetime
import telegram

# 텔레그램 토큰
# 머리돌
telgm_token = '1635387024:AAEQfnk-F5A274EmpY1SSFY8bPYJbdULf2g'

# 모아이대가리
moai_token = '5272244147:AAHpcSWzIapXCNlm7yxW7Xvqs2hLRhU5UGs'


# stoneheadcoding , @daegalibot
# 머리돌 채널 ID  : -1001280712219
stonehead_channel = '-1001280712219'

telgm_bot = telegram.Bot(token = moai_token)

updates = telgm_bot.getUpdates()
print(updates[0].mesage.chat_id)



# Today (Ex:20210228)
today = datetime.today().strftime("%Y%m%d")
todayTime = datetime.today().strftime("%Y%m%d%H%M%S")

# 텔레그램 채널에 메세지 보내기
def telgm_channel_send_msg(channel, msg):
    telgm_bot.sendMessage(chat_id = channel, text=msg)

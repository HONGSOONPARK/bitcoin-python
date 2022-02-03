from module import telegram_bot

import sys
import logging
import traceback
# from module import upbit


import telegram


# 모아이  ID : -1001318811692
moai_chat_id = '-1001318811692'

# -----------------------------------------------------------------------------
# - Name : main
# - Desc : 메인
# -----------------------------------------------------------------------------
if __name__ == '__main__':

    telegram_bot.telgm_channel_send_msg(moai_chat_id, 'testtt')

    try:
        print('test')

    except KeyboardInterrupt:
        print('KeyboardInterrupt Exception')

    except Exception:
        print('Exception')

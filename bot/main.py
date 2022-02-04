from module import telegram_bot
from module import commons
# from module import upbit

import sys
import traceback
import logging


# -----------------------------------------------------------------------------
# - Name : main
# - Desc : 메인, 프로그램 시작점
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    try:
        commons.set_loglevel('D')
        # raise Exception('test 케케 ')

        # item_list = commons.get_items('KRW', '')

        # cur_balance = commons.get_balance('KRW-XEC')

        # get_accounts = commons.get_accounts('Y', 'KRW-XEC')

        # print(get_accounts)

        krw_balance = commons.get_candle('KRW-XEC', '3', 10)
        print(krw_balance)

        # for data_for in item_list:
        #     print(data_for['market'].split('-')[1], data_for['korean_name'])

        # logging.debug(item_list)
        # telegram_bot.telgm_channel_send_msg('-1001318811692', item_list)

    except KeyboardInterrupt as e:
        print('KeyboardInterrupt Exception.', e)
        logging.error(traceback.format_exc())
        sys.exit(1)

    except Exception as e:
        print('Exception.', e)
        logging.error(traceback.format_exc())
        sys.exit(1)

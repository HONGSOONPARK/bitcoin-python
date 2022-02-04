# from module import telegram_bot
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
        print('test')
        commons.set_loglevel('D')
        # raise Exception('test 케케 ')

        item_list = commons.get_items('KRW', '')
        logging.debug(item_list)

    except KeyboardInterrupt as e:
        print('KeyboardInterrupt Exception.', e)
        logging.error(traceback.format_exc())
        sys.exit(1)

    except Exception as e:
        print('Exception.', e)
        logging.error(traceback.format_exc())
        sys.exit(1)

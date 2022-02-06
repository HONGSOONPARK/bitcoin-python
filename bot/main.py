from calendar import c
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
if __name__ == "__main__":
    try:
        commons.set_loglevel("D")
        # raise Exception('test 케케 ')

        # cur_balance = commons.get_balance('KRW-XEC')
        # get_accounts = commons.get_accounts('Y', 'KRW-XEC')
        # print(get_accounts)

        # krw_balance = commons.get_candle('KRW-XEC', '3', 10)
        # print(krw_balance)

        # rsi_data = commons.get_rsi('KRW-BTC', '30', '200')

        # mfi_data = commons.get_mfi('KRW-BTC', '30', '200', 10)

        # for mfi_data_for in mfi_data:
        #     logging.info(mfi_data_for)

        items = commons.get_items("KRW", "")
        logging.info(items)

        # for data_for in item_list:
        #     print(data_for['market'].split('-')[1], data_for['korean_name'])

        # logging.debug(item_list)
        # telegram_bot.telgm_channel_send_msg('-1001318811692', rsi_data)

        # macd_data = commons.get_macd('KRW-BTC', '3', '200', 10)

        # for macd_data_for in macd_data:
        #     logging.info(macd_data_for)

        # ---------------------------------------------------------------------
        # Logic Start!
        # ---------------------------------------------------------------------
        # 볼린저밴드 조회
        # bb_data = commons.get_bb('KRW-BTC', '30', '200', 10)

        # for bb_data_for in bb_data:
        #     logging.info(bb_data_for)

        # ---------------------------------------------------------------------
        # Logic Start!
        # ---------------------------------------------------------------------

        # 3분봉 캔들 200
        indicators = commons.get_indicator_sel(
            "KRW-BTC", "3", 200, 28, ["MACD", "MA", "BB", "CANDLE"]
        )

        # 보조지표 추출
        ma = indicators["MA"]
        macd = indicators["MACD"]
        bb = indicators["BB"]
        # candles = indicators["CANDLE"]

        logging.info(ma)
        logging.info(macd)
        logging.info(bb)

        #

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

    except Exception as e:
        print("Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

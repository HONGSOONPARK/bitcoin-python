import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import telegram_bot
from module import commons
import time
from calendar import c

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

        items = commons.get_items("KRW", "")
        logging.info(items)

        # time.sleep(1.5)

        print(len(items))

        # for index, data in enumerate(items):
        #     if index % 10 == 0:
        #         time.sleep(1.5)
        #         logging.info("api 호출 딜레이..")

        #     print(data["market"], index)

        # 3분봉 캔들 200
        indicators = commons.get_indicator_sel(
            "KRW-BTC", "3", 200, 26, ["MACD", "MA", "BB", "CANDLE"]
        )

        # 보조지표 추출
        ma = indicators["MA"]
        macd = indicators["MACD"]
        bb = indicators["BB"]

        logging.info(ma)
        logging.info(macd)
        logging.info(bb)

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

    except Exception as e:
        print("Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

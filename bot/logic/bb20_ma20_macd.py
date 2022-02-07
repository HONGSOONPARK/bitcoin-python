import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import telegram_bot
from module import commons
import time
import datetime
from calendar import c
import math

# from module import upbit

import sys
import traceback
import logging


def get_market_price(candle):
    msg = ""
    _date = datetime.datetime.fromisoformat(
        (candle[0]["candle_date_time_kst"])
    ).strftime("%Y년%m월%d일 %H시%M분")

    _price = math.trunc(candle[0]["trade_price"])

    msg += _date + "\n종목: " + candle[0]["market"] + "\n현재가: " + str(_price)
    logging.debug(msg)
    # print(time.strftime("%Y%m%d", candle[0]["candle_date_time_kst"]))
    # telegram_bot.moaihead_channel_send_msg(msg)

    return _price


def check_ma20(candle, ma):
    candle_sum = 0
    candle26_avr = 0
    count = 26

    for i in range(0, int(count - 1)):
        candle_sum += ma[i]["MA20"]

    candle26_avr = math.trunc(candle_sum / (count))
    currunt_price = get_market_price(candle)

    # 현재가 - 20일 이동평균선(26개 캔들의 평균) > 0
    per = round(((currunt_price - candle26_avr) * 100) / candle26_avr, 1)
    print(per)
    # per 가 1 이상이면 평행, 우상향으로 판단


def check_macd(candle, macd):
    print(macd[0]["OCL"])


def check_bb(candle, bb):
    print(bb[0]["BBH"])


# -----------------------------------------------------------------------------
# - Name : check_logic
# - Desc : 3분, 캔들 26개 기준, ma20, bb20, macd 확인
# -      : 3분봉상 20일 이동평균선이 평행 혹은 우상향(캔들 26개)
# -      : macd 오실레이터가 0선 위
# -      : 캔들이 볼린져밴드의 기준선 or 상향선을 돌파
# -----------------------------------------------------------------------------
def check_logic():

    while True:

        time.sleep(1.5)

        # 3분봉 캔들 200
        indicators = commons.get_indicator_sel(
            "KRW-BTC", "3", 200, 26, ["MACD", "MA", "BB", "CANDLE"]
        )

        # 보조지표 추출
        candle = indicators["CANDLE"]
        ma = indicators["MA"]
        macd = indicators["MACD"]
        bb = indicators["BB"]

        # check_ma20(candle, ma)
        # check_macd(candle, macd)
        # check_bb(candle, bb)

        # logging.info(candle)
        # logging.info(ma)
        # logging.info(macd)
        # logging.info(bb)

        # 봇 메세지
        msg = ""
        _date = datetime.datetime.fromisoformat(
            (candle[0]["candle_date_time_kst"])
        ).strftime("%Y년%m월%d일 %H시%M분")

        # 현재가
        currunt_price = round(candle[0]["trade_price"], 5)

        msg += _date + "\n종목: " + candle[0]["market"] + "\n현재가: " + str(currunt_price)
        # logging.debug(msg)

        # 캔들 현재값 합
        candle_sum = 0
        # 캔들 26개의 평균
        candle26_avr = 0

        count = 26

        for i in range(0, int(count - 1)):
            candle_sum += ma[i]["MA20"]

        candle26_avr = round(candle_sum / count, 5)
        logging.info(currunt_price)

        # 현재가 - 20일 이동평균선(26개 캔들의 평균) > 0,
        per = round(((currunt_price - candle26_avr) * 100) / candle26_avr, 1)
        msg += "\n20일선과 현재값 차이: " + str(per)
        msg += "\nMACD OCL: " + str(macd[0]["OCL"])
        msg += "\nBBH: " + str(bb[0]["BBH"])

        # per > 1 true
        # ocl > 0 true
        # 현재가가 bb 상단 뚫었을때 true

        if per > 1 and macd[0]["OCL"] > 0 and bb[0]["BBH"] < currunt_price:
            msg += "\n조건: 참 ====> 매수로직 실행"
            telegram_bot.moaihead_channel_send_msg(msg)
        else:
            msg += "\n조건: 만족하지 않음"

        logging.debug(msg)


# -----------------------------------------------------------------------------
# - Name : main
# - Desc : 메인, 프로그램 시작점
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        commons.set_loglevel("D")
        check_logic()
        # items = commons.get_items("KRW", "")
        # logging.info(items)
        # time.sleep(1.5)
        # print(len(items))
        # for index, data in enumerate(items):
        #     if index % 10 == 0:
        #         time.sleep(1.5)
        #         logging.info("api 호출 딜레이..")

        #     print(data["market"], index)

        # 3분봉 캔들 200
        # indicators = commons.get_indicator_sel(
        #     "KRW-BTC", "3", 200, 26, ["MACD", "MA", "BB", "CANDLE"]
        # )

        # # 보조지표 추출
        # candle = indicators["CANDLE"]
        # ma = indicators["MA"]
        # macd = indicators["MACD"]
        # bb = indicators["BB"]

        # # get_market_price(candle)
        # logging.info(candle)
        # logging.info(ma)
        # logging.info(macd)
        # logging.info(bb)

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

    except Exception as e:
        print("Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

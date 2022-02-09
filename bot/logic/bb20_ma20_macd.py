import sys
import os

from numpy import equal

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from module import telegram_bot
from module import commons
import time
import datetime
from calendar import c
import math
import pandas

# from module import upbit

import sys
import traceback
import logging


# 당일 20ma 값과 5일전 값을 비교했을때 양수
# 당일 20ma 값과 10일전 값을 비교했을때 양수
# and
# 5와 10일 전 값과 비교햇을때 양수(뺏을때 양수)
def check_ma20(candle, ma, ticker):

    result = {}
    msg = ""
    today = datetime.datetime.now()

    time.sleep(0.5)
    candle_day = commons.get_candle(ticker, "D", 20)

    # 5일전, 10일전 날짜를 구하고 금액을 변수에 저장

    ago_5days = (today - datetime.timedelta(days=5)).strftime("%Y%m%d")
    ago_5days_price = 0
    ago_10days = (today - datetime.timedelta(days=10)).strftime("%Y%m%d")
    ago_10days_price = 0
    for i in range(0, len(candle_day)):
        candle_date = datetime.datetime.fromisoformat(
            (candle_day[i]["candle_date_time_kst"])
        ).strftime("%Y%m%d")

        if ago_5days == candle_date:
            ago_5days_price = candle_day[i]["trade_price"]

        if ago_10days == candle_date:
            ago_10days_price = candle_day[i]["trade_price"]

    # 현재가격
    trade_price = candle[0]["trade_price"]

    # 현재 MA20 가격
    ma20_price = ma[0]["MA20"]

    msg += "\n5일전 가격 : " + str(ago_5days_price)
    msg += "\n10일전 가격 : " + str(ago_10days_price)
    msg += "\n20이평선 가격 " + str(ma20_price)

    result["msg"] = msg

    if (
        ago_5days_price - ma20_price > 0
        and ago_10days_price - ma20_price > 0
        and ago_5days_price - trade_price > 0
        and ago_10days_price - trade_price > 0
    ):
        result["result"] = True
        return result

    else:
        result["result"] = False
        return result


# 당일 20ma 값과 5일전 값을 비교했을때 양수
# 당일 20ma 값과 10일전 값을 비교했을때 양수
# and
# 5와 10일 전 값과 비교햇을때 양수(뺏을때 양수)
def check_ma20_v2(ticker):

    result = {}
    msg = ""
    today = datetime.datetime.now()

    time.sleep(0.5)

    # Call 일봉 캔들 200
    indicators = commons.get_indicator_sel(ticker, "D", 200, 26, ["MA", "CANDLE"])

    # 일봉 보조지표 추출
    candle = indicators["CANDLE"]
    ma = indicators["MA"]

    # 현재가격
    trade_price = candle[0]["trade_price"]

    # 현재 MA20 가격
    ma20_price = ma[0]["MA20"]
    ma20_5ago = ma[5]["MA20"]
    ma20_10ago = ma[10]["MA20"]

    msg += "\n금일 MA20 " + str(ma20_price)
    msg += "\n5일전 MA20 " + str(ma20_5ago)
    msg += "\n10일전 MA20 " + str(ma20_10ago)

    result["msg"] = msg

    if ma20_price - ma20_5ago > 0 and ma20_price - ma20_10ago > 0:
        result["result"] = True
        return result

    else:
        result["result"] = False
        return result


# -----------------------------------------------------------------------------
# - Name : check_logic
# - Desc : 3분, 캔들 26개 기준, ma20, bb20, macd 확인
# -      : 3분봉상 20일 이동평균선이 평행 혹은 우상향(캔들 26개)
# -      : macd 오실레이터가 0선 위
# -      : 캔들이 볼린져밴드의 기준선 or 상향선을 돌파
# -----------------------------------------------------------------------------
def check_logic():

    ticker = "KRW-BTC"

    while True:
        # 봇 메세지
        msg = ""
        # Call 3분봉 캔들 200
        indicators = commons.get_indicator_sel(
            ticker, "3", 200, 26, ["MACD", "MA", "BB", "CANDLE"]
        )

        # 보조지표 추출
        candle = indicators["CANDLE"]
        ma = indicators["MA"]
        macd = indicators["MACD"]
        bb = indicators["BB"]

        now = (datetime.datetime.now()).strftime("%Y년%m월%d일 %H시%M분%S초")

        # 현재가
        currunt_price = round(candle[0]["trade_price"], 5)

        msg += (
            "\n" + now + "\n종목: " + candle[0]["market"] + "\n현재가: " + str(currunt_price)
        )
        # logging.debug(msg)

        ma20_result = check_ma20_v2(ticker)

        msg += ma20_result["msg"]
        msg += "\nMA 검증 결과: " + str(ma20_result["result"])
        msg += "\nMACD OCL: " + str(macd[0]["OCL"])
        msg += "\nBBH: " + str(bb[0]["BBH"])

        # ocl > 0 true
        # 현재가가 bb 상단 뚫었을때 true
        if (
            ma20_result["result"] == True
            and macd[0]["OCL"] > 0
            and bb[0]["BBH"] < currunt_price
        ):

            msg += "\n================="
            msg += "\n조건: 참 ====> 매수로직 실행"
            msg += "\n================="
            telegram_bot.stonehead_channel_send_msg(msg)
        else:
            msg += "\n================="
            msg += "\n조건: 만족하지 않음"
            msg += "\n================="

        logging.info(msg)
        # 10초 딜레이
        time.sleep(10.0)


# -----------------------------------------------------------------------------
# - Name : main
# - Desc : 메인, 프로그램 시작점
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    try:
        commons.set_loglevel("D")
        check_logic()
        # check_ma20_v2("KRW-BTC")

        # items = commons.get_items("KRW", "")
        # logging.info(items)
        # time.sleep(1.5)
        # print(len(items))
        # for index, data in enumerate(items):
        #     if index % 10 == 0:
        #         time.sleep(1.5)
        #         logging.info("api 호출 딜레이..")

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

    except Exception as e:
        print("Exception.", e)
        logging.error(traceback.format_exc())
        sys.exit(1)

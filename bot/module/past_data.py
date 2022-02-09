import pyupbit
import pandas as pd


# tickers = pyupbit.get_tickers()
upbit = pyupbit.Upbit(access_key, secret_key)
# print(tickers)

df = pyupbit.get_ohlcv("KRW-BTC")
pd.DataFrame(df)
df.to_excel("btc_history.xlsx")

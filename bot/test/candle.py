import requests

url = "https://api.upbit.com/v1/candles/minutes/3?market=KRW-BTC&count=200"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)

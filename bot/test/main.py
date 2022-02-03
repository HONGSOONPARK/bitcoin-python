# access key :  
# secret key :  


# import pyupbit
# tickers = pyupbit.get_tickers(fiat="KRW")
# print(tickers)


# price = pyupbit.get_current_price("KRW-XEC")
# print(price)


import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello")
label.show()
app.exec_()

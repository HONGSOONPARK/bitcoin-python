import datetime
import backtrader as bt
import backtrader.feeds as btfeeds
import locale


class SmaCross(bt.Strategy):  # bt.Strategy를 상속한 class로 생성해야 함.
    params = dict(
        pfast=5,  # period for the fast moving average
        pslow=30,  # period for the slow moving average
    )

    def __init__(self):
        sma1 = bt.ind.SMA(period=self.p.pfast)  # fast moving average
        sma2 = bt.ind.SMA(period=self.p.pslow)  # slow moving average
        self.crossover = bt.ind.CrossOver(sma1, sma2)  # crossover signal
        self.holding = 0

    def next(self):
        current_stock_price = self.data.close[0]

        if not self.position:  # not in the market
            if self.crossover > 0:  # if fast crosses slow to the upside
                available_stocks = self.broker.getcash() / current_stock_price
                self.buy(size=1)
            elif self.crossover < 0:  # in the market & cross to the downside
                self.close()  # close long position

    def notify_order(self, order):
        if order.status not in [order.Completed]:
            return

        if order.isbuy():
            action = "Buy"
        elif order.issell():
            action = "Sell"

        stock_price = self.data.close[0]
        cash = self.broker.getcash()
        value = self.broker.getvalue()
        self.holding += order.size

        print(
            "%s[%d] holding[%d] price[%d] cash[%.2f] value[%.2f]"
            % (action, abs(order.size), self.holding, stock_price, cash, value)
        )


cerebro = bt.Cerebro()  # create a "Cerebro" engine instance
cerebro.broker.setcash(100000)
cerebro.broker.setcommission(0.002)


data = btfeeds.GenericCSVData(
    dataname="btc_history.csv",
    fromdate=datetime.datetime(2021, 7, 25),
    todate=datetime.datetime(2022, 2, 9),
    nullvalue=0.0,
    dtformat=("%Y-%m-%d %H:%M:%S"),
    datetime=0,
    high=1,
    low=2,
    open=3,
    close=4,
    volume=5,
    openinterest=-1,
)

cerebro.adddata(data)  # Add the data feed

cerebro.addstrategy(SmaCross)  # Add the trading strategy

start_value = cerebro.broker.getvalue()
cerebro.run()  # run it all
final_value = cerebro.broker.getvalue()

print("* start value : %s won" % locale.format_string("%d", start_value, grouping=True))
print("* final value : %s won" % locale.format_string("%d", final_value, grouping=True))
print("* earning rate : %.2f %%" % ((final_value - start_value) / start_value * 100.0))

cerebro.plot()  # and plot it with a single command

import backtrader as bt
import alpaca_backtrader_api
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt # no error, it works
plt.figure(1).show()
import pandas as pd
import Tkinter

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=10), bt.ind.SMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)
print(0)
cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)
print(1)
store = alpaca_backtrader_api.AlpacaStore(
    key_id='PKTN99XWM1SQATZ28PBM',
    secret_key='mvAMEH6usShrMzFYWtvlHT5v97OeC7eIQ5J6/QWn',
    paper=True
)
print(2)
broker = store.getbroker()  # or just alpaca_backtrader_api.AlpacaBroker()
cerebro.setbroker(broker)
print(3)
DataFactory = store.getdata # or use alpaca_backtrader_api.AlpacaData
#data0 = DataFactory(dataname='AAPL', timeframe=bt.TimeFrame.TFrame("Days"))  # Supported timeframes: "Days"/"Minutes"
data0 = DataFactory(
    dataname='AAPL',
    timeframe=bt.TimeFrame.TFrame("Minutes"),
    fromdate=pd.Timestamp('2018-11-15'),
    todate=pd.Timestamp('2018-11-17'),
    historical=True)
cerebro.adddata(data0)
cerebro.adddata(data0)
print(4)
cerebro.run(exactbars=-1) # or -1 or -2
print("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())
cerebro.plot()[0][0]
print(5)
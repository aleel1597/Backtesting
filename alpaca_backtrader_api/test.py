import backtrader as bt
import alpaca_backtrader_api
import pandas as pd

API_KEY = "PKTN99XWM1SQATZ28PBM"
API_SECRET = "mvAMEH6usShrMzFYWtvlHT5v97OeC7eIQ5J6/QWn"
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"


class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.EMA(period=10), bt.ind.EMA(period=30)
        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()
cerebro.addstrategy(SmaCross)

store = alpaca_backtrader_api.AlpacaStore(
    key_id=API_KEY,
    secret_key=API_SECRET,
    paper=APCA_API_BASE_URL
)

cerebro.broker.setcash(100000)
cerebro.broker.setcommission(commission=0.0)
cerebro.addsizer(bt.sizers.PercentSizer, percents=90)

DataFactory = store.getdata # or use alpaca_backtrader_api.AlpacaData
data0 = DataFactory(
    dataname='MSFT',
    timeframe=bt.TimeFrame.Days,
    fromdate=pd.Timestamp('2018-2-1'),
    todate=pd.Timestamp('2019-12-15'),
    historical=True)
cerebro.adddata(data0)

cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()
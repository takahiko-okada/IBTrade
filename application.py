from ib_insync import *
import time

def onPendingTickers(tickers):
    for t in tickers:
        print(t.bidSize, t.bid, t.ask, t.askSize, t.high, t.low, t.close)

if __name__ == "__main__":
    ib = IB()
    ib.connect('127.0.0.1', 4001, clientId=1)
    contracts = [Forex(pair) for pair in 'EURUSD USDJPY GBPUSD USDCHF USDCAD AUDUSD'.split()]
    eurusd = contracts[0]
    for contract in contracts:
        ib.reqMktData(contract, '', False, False)
    ib.pendingTickersEvent += onPendingTickers
    while True:
        ib.sleep(1)

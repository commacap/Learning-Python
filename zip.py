#zip() combines items placed positinally in an iterable into a tuple(Combines)
money_mkt = ['Bonds','Bills', 'Fixed deposits']
equities = ['KCB', 'Tesla', 'Alibaba']
etfs = ['VOO','QQQ','ABSA']

def portfolio():
 print(list(zip(money_mkt, equities, etfs)))

portfolio()
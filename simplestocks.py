#simple stocks python code -sarah karodia, run in terminal >python simplestocks.py
#08-12-2017
import time
import datetime
import math

#create stock class
class Stock():
    symbol = '' 
    type = ''
    last_div= 0
    fixed_div = 0
    par_val = 0

#functions that have market price as input,
    def div_yield(self, price):
        if price == 0: return 0 
        else: 
            if self.type == 'Common': return self.last_div/price
            elif self.type == 'Preferred': return (self.fixed_div*self.par_val)/price
            else: return 0

    def PE_ratio(self, price):
        if self.last_div == 0: return 0
        else: return price/self.last_div

#Class trade, 
class Trade():
    stock = Stock()
    buy = True #if buy is False => sell
    number = 0
    price = 0
    ts = datetime.datetime.now()


#class exchange with list of stocks and trades
class  Exchange():
    stocks = [] #list of stocks
    trades = [] #list of trades
    def add_stock(self, Stock1):
        self.stocks.append(Stock1)
        return 0
        
    def list_stocks(self):
        return self.stocks


    def add_trade(self, Trade1):
        self.trades.append(Trade1)
        return 0
    
    def list_trades(self):
        return self.trades

    #for Stock1 in time frame of last n  minutes
    def Vol_W(self, Stock1, n):
        num = 0
        dom = 0
        for t in self.trades:
            if (t.ts - datetime.datetime.now() < datetime.timedelta(minutes=n)) and Stock1 == t.stock:
                num += t.price*t.number
                dom += t.number
        if dom==0: return 0
        else: return num/dom

    #geometric mean in time frame of last n  minutes 
    def geom_mean(self,n):
        gmn = 1.
        arr = [] #array for containing stocks in trades only
        #if there are trades in this stock
        for t in self.trades:
            if t.stock in self.stocks:
                arr.append(t.stock)
        arr2 = list(set(arr))#orderd list with no duplicates
        for s in arr2: #loop over all stock types in trades.
            gmn = gmn*self.Vol_W(s,n)
        gm = gmn**(1/float(len(arr2)))
        return gm


#rest of sript dealing with information given in qu
tea = Stock()
tea.type = 'Common'; tea.last_div = 0.; tea.par_val = 100.
pop = Stock()
pop.type = 'Common'; pop.last_div = 8.; pop.par_val = 100.
ale = Stock()
ale.type = 'Common'; ale.last_div = 23.; ale.par_val = 60.
gin = Stock()
gin.type = 'Preferred'; gin.last_div = 8.; gin.fixed_div = 0.02; gin.par_val = 100.
joe=Stock()
joe.type = 'Common'; joe.last_div = 13.; joe.par_val = 250.



print('div yield tea', tea.div_yield(10.))
print('div yield pop', pop.div_yield(10.))
print('div yield gin', gin.div_yield(10.))

print('P/E tea', tea.PE_ratio(10.))
print('P/E pop', pop.PE_ratio(10.))
print('P/E gin', gin.PE_ratio(10.))

#trades
t1 = Trade()
t1.stock = pop; t1.buy = True; t1.number= 5.; t1.price =10.; t1.ts = datetime.datetime.now()
t2 = Trade()
t2.stock = joe; t2.buy = True; t2.number= 7.; t2.price =60.; t2.ts = datetime.datetime.now()
t3 = Trade()
t3.stock = pop; t3.buy = True; t3.number= 6.; t3.price =15.; t3.ts = datetime.datetime.now()
#exchange
x = Exchange()
x.add_stock(tea); x.add_stock(pop); x.add_stock(ale);x.add_stock(gin); x.add_stock(joe)
x.add_trade(t1); x.add_trade(t2); x.add_trade(t3)
#print(x.list_trades())
print('t1 time', t1.ts)
print('t2 time', t2.ts)
print('t3 time', t3.ts)
print('pop Volume Weighted Stock Price',x.Vol_W(pop, 15))
print('joe Volume Weighted Stock Price',x.Vol_W(joe, 15))
print('geometric mean',x.geom_mean(15))


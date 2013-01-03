# portfolio.py
import stock

class Portfolio(object):
    def __init__(self,filename=None):
        if filename:
             self.holdings = stock.read_portfolio(filename)
        else:
             self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()

    def cost(self):
        return sum([s.shares*s.price for s in self.holdings])

if __name__ == '__main__':
    port = Portfolio("../../Data/portfolio.dat")
    for s in port:
        print s
    print "Cost:", port.cost()

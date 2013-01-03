# stock.py

class Stock(object):
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self,name,shares,price):
        self.name   = name
        self.shares = shares
        self.price  = price

    def cost(self):
        '''
        Return the cost as shares*price
        '''
        return self.shares*self.price

    def sell(self,nshares):
        '''
        Sell a number of shares and return the remaining number.
        '''
        self.shares -= nshares
        return self.shares

def read_portfolio(filename):
    '''
    Read a portfolio file into a list of stock instances.
    '''
    portfolio = []
    for line in open(filename):
        fields = line.split()
        holding = Stock(fields[0],int(fields[1]),float(fields[2]))
        portfolio.append(holding)
    return portfolio

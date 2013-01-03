# stock.py
#
# Part (b) Solution

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

class PortfolioPrinter(object):
    '''
    Output portfolio data in plain-text format.
    '''
    def print_table(self,portfolio):
        '''
        Make a nicely formatted table showing portfolio contents.
        '''
        self.headings(['Name','Shares','Price'])
        for s in portfolio:
            self.row([s.name, "%d" % s.shares, "%0.2f" % s.price])

    def headings(self,headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print "%10s" % h,
        print
        print ("-"*10 + " ")*len(headers)

    def row(self,rowdata):
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print "%10s" % d,
        print

if __name__ == '__main__':
    portfolio = read_portfolio("../../Data/portfolio.dat")
    printer = PortfolioPrinter()
    printer.print_table(portfolio)

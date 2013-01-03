# report.py

import fieldparse

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    return fieldparse.parse(open(filename),[str,int,float],['name','shares','price'])

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    return dict(fieldparse.parse(open(filename),[str,float],sep=','))

def make_report(portfolio,prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change        = current_price - stock['price']
        summary       = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name','Shares','Price','Change')
    print ("%10s " * len(headers)) % headers
    print ("-"*10 + " ")*len(headers)
    for row in reportdata:
        print "%10s %10d %10.2f %10.2f" % row

def portfolio_report(portfoliofile,pricefile):        
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files 
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)

    # Create the report data
    report    = make_report(portfolio,prices)

    # Print it out
    print_report(report)

if __name__ == '__main__':
    portfolio_report("../../Data/portfolio.dat",
                     "../../Data/prices.csv")

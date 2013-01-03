# report.py

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    f = open(filename)
    for line in f:
        fields = line.split()
        stock = {
             'name'   : fields[0],
             'shares' : int(fields[1]),
             'price'   : float(fields[2])
        }
        portfolio.append(stock)
    f.close()
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    f = open(filename)
    for line in f:
        fields = line.split(",")
        try:
            name = fields[0].strip('"')
            prices[name] = float(fields[1])
        except IndexError:
            pass
    f.close()
    return prices

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
        
# Read data files and create the report data        

portfolio = read_portfolio("../../Data/portfolio.dat")
prices    = read_prices("../../Data/prices.csv")

# Generate the report data

report    = make_report(portfolio,prices)

# Output the report
headers = ('Name','Shares','Price','Change')
print ("%10s " * len(headers)) % headers
print ("-"*10 + " ")*len(headers)
for row in report:
    print "%10s %10d %10.2f %10.2f" % row

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

portfolio = read_portfolio("../../Data/portfolio.dat")
prices    = read_prices("../../Data/prices.csv")

# Calculate the total cost of the portfolio
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print "Total cost", total_cost

# Compute the current value of the portfolio
total_value = 0.0
for s in portfolio:
    total_value += s['shares']*prices[s['name']]

print "Current value", total_value
print "Gain", total_value - total_cost

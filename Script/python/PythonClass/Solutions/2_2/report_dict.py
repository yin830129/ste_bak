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



# Calculate the total cost of the portfolio
portfolio = read_portfolio("../../Data/portfolio.dat")

total_cost = 0.0
for s in portfolio:
    total_cost += s['shares']*s['price']

print "Total cost", total_cost

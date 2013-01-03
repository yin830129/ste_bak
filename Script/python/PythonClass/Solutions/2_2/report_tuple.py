# report.py

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of (name, shares, price) tuples.
    '''
    portfolio = []
    f = open(filename)
    for line in f:
        fields  = line.split()
        stock = (fields[0],int(fields[1]),float(fields[2]))
        portfolio.append(stock)
    f.close()
    return portfolio

# Calculate the total cost of the portfolio
portfolio = read_portfolio("../../Data/portfolio.dat")

total_cost = 0.0
for s in portfolio:
    total_cost += s[1]*s[2]

print "Total cost", total_cost

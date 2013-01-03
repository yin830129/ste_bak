# stock.py
#
# Part (d) Solution



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

class CSVPortfolioPrinter(PortfolioPrinter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self,headers):
        print ",".join(headers)
    def row(self,rowdata):
        print ",".join(rowdata)

class HTMLPortfolioPrinter(PortfolioPrinter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self,headers):
        print "<tr>",
        for h in headers:
            print "<th>%s</th>" % h,
        print "</tr>"
    def row(self,rowdata):
        print "<tr>",
        for d in rowdata:
            print "<td>%s</td>" % d,
        print "</tr>"

if __name__ == '__main__':
    portfolio = read_portfolio("../../Data/portfolio.dat")
    fmt = raw_input("Output format [text|csv|html] : ")
    if fmt == 'text':
        printer = PortfolioPrinter()
    elif fmt == 'csv':
        printer = CSVPortfolioPrinter()
    elif fmt == 'html':
        printer = HTMLPortfolioPrinter()
    else:
        raise RuntimeError("Unsupported output format")
    printer.print_table(portfolio)

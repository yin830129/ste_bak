# stock.py

class Stock(object):
    def __init__(self,name,shares,price):
        self.name   = name
        self.shares = shares
        self.price  = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
    def __repr__(self):
         return "Stock(%r,%r,%r)" % (self.name,self.shares,self.price)

if __name__ == '__main__':
    import fieldparse
    portfolio = fieldparse.parse(open("../../Data/portfolio.dat"),[str,int,float],constructor=Stock)
    for s in portfolio:
        print s

# pcost.py

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    f = open(filename)
    for line in f:
        fields = line.split()
        try:
            nshares    = int(fields[1])
            price      = float(fields[2])
            total_cost = total_cost + nshares*price

        # This catches errors in int() and float() conversions above
        except ValueError:
            print "Bad line:", line
        except IndexError:
            # pass does nothing.   We use it to ignore the exception
            pass

    f.close()
    return total_cost

import glob
filelist = glob.glob("../../Data/portfolio*.dat")

for name in filelist:
    cost = portfolio_cost(name)
    print name, cost

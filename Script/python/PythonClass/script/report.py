# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:57:06 2012

@author: hewu
"""

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
    
portfolio=read_portfolio("Data/portfolio.dat")
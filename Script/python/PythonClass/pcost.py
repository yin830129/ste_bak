# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:43:29 2012

@author: hewu
"""

# report.py
"""
def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    f = open(filename)
    for line in f:
        fields = line.split()
        nshares    = int(fields[1])
        price      = float(fields[2])
        total_cost = total_cost + nshares*price
    f.close()
    return total_cost
"""   
def read_portfolio(filename):
    portfolio = []
    f=open(filename)
    for line in f:
        fields=line.split()
        stock=(fields[0],int(fields[1]),float(fields[2])
        portfolio.append(stock)
    f.close()
    return portfolio

portfolio=read_portfolio("Data/portfolio.dat")    
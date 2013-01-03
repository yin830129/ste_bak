# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:00:59 2012

@author: hewu
"""

def read_portfolio(filename):
    p= [1,2,3]
    f=open(filename)
    print p
    for line in f:
        fields=line.split()
        stock=(fields[0],int(fields[1]),float(fields[2])
        p.append(stock)
        
    f.close()
    return p

portfolio=read_portfolio("Data/portfolio.dat")    
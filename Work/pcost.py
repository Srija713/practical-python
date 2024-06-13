# pcost.py
#
# Exercise 1.27
import csv
# a csv(comma separated value) file is a txt file which has data separated by commas
import sys #used to read command line arguments
def portfolio_cost(filename):
    cost=0
    f=open(filename,'rt') 
    header=next(f) 
    for row in f:
        li=row.split(',')
        cost=cost+(float(li[1])*float(li[2]))
    f.close()
    return cost
if len(sys.argv)==2:
    filename=sys.argv[1]
else:
    filename='Data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
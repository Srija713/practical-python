# pcost.py
#
# Exercise 1.27
import csv
def portfolio_cost(filename):
    cost=0
    f=open(filename)
    rows=csv.reader(f)
    header=next(rows)
    for li in rows:
        cost=cost+(float(li[1])*float(li[2]))
    f.close()
    return cost
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
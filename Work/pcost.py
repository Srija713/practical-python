# pcost.py
#
# Exercise 1.27
import csv
# a csv(comma separated value) file is a txt file which has data separated by commas
def portfolio_cost(filename):
    cost=0
    f=open(filename)
    rows=csv.reader(f) #converts each line into a list(works like split(,))
    header=next(rows) #reads the upcoming line in this case first line
    for li in rows:
        cost=cost+(float(li[1])*float(li[2]))
    f.close()
    return cost
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
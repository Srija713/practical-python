# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    cost=0
    with open(filename, 'rt') as f:
        header=next(f)
        for line in f:
            li=line.split(',')
            cost=cost+(float(li[1])*float(li[2]))
    f.close()
    return cost
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
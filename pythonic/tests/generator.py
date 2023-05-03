colors = ['black', 'white', 'wellow', 'Brown']
sizes = ['S', 'M', 'L', 'XL']
for shirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(shirt)
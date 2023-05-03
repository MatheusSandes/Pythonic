import math
import operator
list1 = [1, 4, 9, 16, 25, 36]
list2 = map(math.sqrt, list1)
soma = reduce(operator.add, list1)

def bigger_then_8(x):
    return x > 8
print(filter(bigger_then_8, list1))
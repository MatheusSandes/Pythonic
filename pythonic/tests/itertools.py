
# Python program to demonstrate
# infinite iterators
   
import itertools
   
count = 0
   
# for in loop
for i in itertools.cycle('ABC'):
    if count > 5:
        break
    else:
        print(i, end = " ")
        count += 1
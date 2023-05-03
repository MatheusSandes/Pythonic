# Python code to demonstrate working of  
# pop(), and popleft() 
  
from collections import deque
  
# initializing deque 
d = deque([8, 3, 5, 2, 9])

# using pop() to delete element from right end  
# deletes 4 from the right end of deque 
d.pop()
    
# printing modified deque 
print ("The deque after deleting from right is : ") 
print (d)
    
# using popleft() to delete element from left end  
# deletes 6 from the left end of deque 
d.popleft()
    
# printing modified deque 
print ("The deque after deleting from left is : ") 
print (d)
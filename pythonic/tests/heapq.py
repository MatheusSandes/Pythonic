import heapq

l = [5, 7, 9, 1, 3, 2, 6]
 
# using heapify to convert list into heap
heapq.heapify(l)
 
# printing created heap
print ("The created heap is : ",end="")
print (list(l))
 
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(l,4)
 
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(l))
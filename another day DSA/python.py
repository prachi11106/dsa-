# import array as arr
# # to find maximum value in an array
# arr = [12, 7, 8, 9, 0]

# max_val = arr[0] # we consider 0th index value as maximum value
# for i in range(1, len(arr)): # loop starts from 1 as we have already considered 0th index
#     if arr[i] > max_val:
#         max_val = arr[i]

# print(max_val)

# # to find second maximum value in an array
# arr = [12, 7 , 8, 9, 0 ]   

# max_val = float('-inf')  # Initialize to the smallest possible value        
# second_max = float('-inf')  # Initialize to the smallest possible value
# for i in range(len(arr)):
#     if arr[i] > max_val:
#         second_max = max_val
#         max_val = arr[i]
#     elif arr[i] > second_max and arr[i] != max_val:
#         second_max = arr[i]
# print( second_max)

# #same with sort method
# arr = [12, 7 , 8, 9, 0 ]
# arr.sort()
# print(arr[-2]) 

# #sir solution
# import math
# firstmax = -math.inf
# secondmax = -math.inf

# for curValue in arr:
#     if curValue > firstmax:
#         secondmax = firstmax
#         firstmax = curValue
#     elif curValue > secondmax:
#         secondmax = curValue
# print(secondmax)

#to find second minimum value in an array
# arr = [12, 7 , 8, 9, 0 ]    

# arr = [12, 35, 1, 10, 2]

# min1 = float('inf')
# min2 = float('inf')

# for num in arr:
#     if num < min1:
#         min2 = min1
#         min1 = num
#     elif num < min2 and num != min1:
#         min2 = num

# print( min2)

# class solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#        dict = {}
#        for i in range(len (nums)):
#            need = target - nums[i]

#            if need in dict:
#                 return [dict[need], i]
           
#            dict[nums[i]] = i
# to print upper triangle of matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
for i in range(len(matrix)):
    for j in range(i, len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
# to print lower triangle of matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):    
    for j in range(i + 1):
        print(matrix[i][j], end=' ')
    print()

n = int(input("Enter number: "))
fact = 1

for i in range(1, n+1):
    fact = fact * i

print("Factorial:", fact)
arr = [10, 20, 30, 40, 50]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        break
def insert_begin(head, data):
    new_node = Node(data)
    
    if head != None:
        head.prev = new_node
        new_node.next = head
        
    head = new_node
    return head
def display(head):
    temp = head
    
    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):       # Add to back
        self.queue.append(item)    # O(1)

    def dequeue(self):             # Remove from front
        if not self.is_empty():
            return self.queue.popleft()  # O(1)

    def front(self):               # View front
        return self.queue[0] if self.queue else None

    def is_empty(self):
        return len(self.queue) == 0

q = Queue()
q.enqueue('A'); q.enqueue('B'); q.enqueue('C')
print(q.dequeue())    # → 'A' (first in, first out)
print(q.dequeue())    # → 'B'
import heapq

# Min-heap: smallest element has highest priority
pq = []
heapq.heappush(pq, (3, 'low priority'))     # (priority, item)
heapq.heappush(pq, (1, 'high priority'))
heapq.heappush(pq, (2, 'medium priority'))

while pq:
    priority, item = heapq.heappop(pq)
    print(f'Priority {priority}: {item}')
# Output: 1: high → 2: medium → 3: low

# For max-heap, negate priorities
heapq.heappush(pq, (-5, 'most important'))








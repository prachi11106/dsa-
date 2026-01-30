import array as arr
# to find maximum value in an array
arr = [12, 7, 8, 9, 0]

max_val = arr[0] # we consider 0th index value as maximum value
for i in range(1, len(arr)): # loop starts from 1 as we have already considered 0th index
    if arr[i] > max_val:
        max_val = arr[i]

print(max_val)

# to find second maximum value in an array
arr = [12, 7 , 8, 9, 0 ]   

max_val = float('-inf')  # Initialize to the smallest possible value        
second_max = float('-inf')  # Initialize to the smallest possible value
for i in range(len(arr)):
    if arr[i] > max_val:
        second_max = max_val
        max_val = arr[i]
    elif arr[i] > second_max and arr[i] != max_val:
        second_max = arr[i]
print( second_max)

#same with sort method
arr = [12, 7 , 8, 9, 0 ]
arr.sort()
print(arr[-2]) 

#sir solution
import math
firstmax = -math.inf
secondmax = -math.inf

for curValue in arr:
    if curValue > firstmax:
        secondmax = firstmax
        firstmax = curValue
    elif curValue > secondmax:
        secondmax = curValue
print(secondmax)

#to find second minimum value in an array
arr = [12, 7 , 8, 9, 0 ]    

arr = [12, 35, 1, 10, 2]

min1 = float('inf')
min2 = float('inf')

for num in arr:
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2 and num != min1:
        min2 = num

print( min2)

class solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       dict = {}
       for i in range(len (nums)):
           need = target - nums[i]

           if need in dict:
                return [dict[need], i]
           
           dict[nums[i]] = i
           









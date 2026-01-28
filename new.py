#QUESTIONS
import array as prachi

arrayName =prachi.array('i',[ 12 , 34, 56, 78])

#for i in range (0,len(arrayName),2): #time complexity O(n)
   # print(arrayName[i],end="")

#write program to get the sum and pro
sum = 0
product = 1 
for i in range (0,len(arrayName)):
    sum = sum + arrayName[i]
    product = product * arrayName[i]    
print("Sum is:",sum)
print("Product is:",product)  

#write program to count target value in array
count = 0
target = int(input("Enter target value:"))
for i in range (0,len(arrayName)):
    if arrayName[i] == target:
        count = count + 1   
print("Count of target value is:",count)

#to check if array is sorted forward or backward or not at all 
is_sorted_asc = True
is_sorted_desc = True       
for i in range (0,len(arrayName)-1):
    if arrayName[i] > arrayName[i+1]:
        is_sorted_asc = False
    if arrayName[i] < arrayName[i+1]:
        is_sorted_desc = False
if is_sorted_asc:
    print("Array is sorted in ascending order")
elif is_sorted_desc:
    print("Array is sorted in descending order") 

#inc=true 
# dec=true   
#For i in range (0,len(arrayName)):
# if(arrayName[i] < arrayName[i+1]):
     #inc= False
# if(arrayName[i] > arrayName[i+1]):
     #dec= False
# if(inc== True):
     #print("Array is sorted in ascending order")   
# elif(dec== True):
     #print("Array is sorted in descending order")
#else:
 #   print("Array is not sorted")
 
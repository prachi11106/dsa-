import array as arr

arrName = arr.array('i', [10, 20, 30, 40, 50])

#operation

#1 add 
# a) append() - adds an element at the end of the array ,T/c- O(1),O(N)
arrName.append(60)  
print("After append:", arrName)
arrName.insert(2, 25)
# b) insert() - adds an element at the specified position,T/C-O(1),O(n)
print("After insert:", arrName)
#remove 
arrName.remove(20)
print(arrName)
# time complexity= O(1) shifting from last position ,
#  O(n) shifting from first position , O(n/2) shifting from middle

#pop method = delete last value by default and if index value given then remove that particular value
arrName.pop(3)
print (arrName)
arrName[2]=52 #update values
print (arrName)

for i in range (0,len(arrName)):
    print(arrName[i],end="")

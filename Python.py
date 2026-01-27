import array as arr

arrName = arr.array('i', [10, 20, 30, 40, 50])

#operation

#1 add 
# a) append() - adds an element at the end of the array
arrName.append(60)  
print("After append:", arrName)
arrName.insert(2, 25)  # b) insert() - adds an element at the specified position
print("After insert:", arrName)
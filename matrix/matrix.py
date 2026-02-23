# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         value = int(input(f"Enter element at position ({i}, {j}): "))
#         row.append(value)
#     matrix.append(row)
# print(matrix)
# #to traversal the matrix
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()
#traversal - visitng each element of the matrix/loop through each element of the matrix/array  
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))  
# matrix = []
# for i in range(rows):   
#     row = []
#     for j in range(cols):
#         value = int(input(f"Enter element at position ({i}, {j}): "))
#         row.append(value)
#     matrix.append(row)  
#rowise traversal   
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()
#columnwise traversal
# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=" ")
#     print()
#  traversal of primary diagonal
# for i in range(rows):
#     print(matrix[i][j], end="")
#  traversal of secondary diagonal
# for i in range(rows):
#     print(matrix[i][cols - 1 - i], end="")

# write a program to calculate sum of each row individually
# for i in range(rows):
#     row_sum = 0       
#     for j in range(cols):
#         row_sum += matrix[i][j]
#     print(f"Sum of row {i}: {row_sum}")   
# #sum of primary diagonal
# primary_diagonal_sum = 0    
# for i in range(rows):
#     primary_diagonal_sum += matrix[i][i]
# print(f"Sum of primary diagonal: {primary_diagonal_sum}")
#sum of secondary diagonal
# secondary_diagonal_sum = 0
# for i in range(rows):
#     secondary_diagonal_sum += matrix[i][cols - 1 - i]   
# print(f"Sum of secondary diagonal: {secondary_diagonal_sum}")


# #18february2026
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))

# matrix = []

# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(int(input(f"Enter element [{i}][{j}]: ")))
#     matrix.append(row)

# transpose = []
# for i in range(cols):
#     temp = []
#     for j in range(rows):
#         temp.append(matrix[j][i])
#     transpose.append(temp)

# for i in range(len(transpose)):
#     transpose[i].reverse()

# for row in transpose:
#     print(*row)
# #1. transpose of the matrix
# for r in range(rows):
#     for c in range(cols):
#         transpose[c][r] = matrix[r][c]

# #2. reverse each row of the transposed matrix
# for r in range(cols):
#     transpose[r].reverse()
# print("The rotated matrix is:")

#rotate the matrix 90 degree anticlockwise
#1.)transpose of the matrix
# for r in range(rows):
#     for c in range(cols):
#         transpose[c][r] = matrix[r][c]
# #2.)reverse the order of each row of the transposed matrix
# for r in range(rows):
#     transpose[r].reverse()
# print("The rotated matrix is:")
#23february2026
# structure of node of linked list (imp)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None    
# #traversal of linked list
# def traverse(self, head):
#     current = head
#     while current is not None:
#         print(current.data, end=" ")
#         current = current.next  
# #sirsolution
# def traversal(self):
#     currentNode = self.head
#     while currentNode is not None:
#         print(currentNode.data, end=" ")
#         currentNode = currentNode.next
class Node:
    def __init__(self, mydata):
        self.data = mydata
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insertFirstPosition(self, mydata):
        new_node = Node(mydata)
        new_node.next  = self.head
        self.head = new_node

    def traversal(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data, end=" ")
            currentNode = currentNode.next
mylist = LinkedList()
mylist.insertFirstPosition(10)
mylist.insertFirstPosition(20)      
mylist.insertFirstPosition(30)

mylist.traversal()
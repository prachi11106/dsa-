# n = int(input("enter a number:"))
# temp = nrev=0

# while n!= 0:
#     digit = n%10
#     nrev = nrev*10 + digit
#     n = n//10
# if temp == nrev:
#     print("palindrome")
# else:
#     print("not palindrome")

# n = int(input("enter a number:"))
# sum = 0
# while n!= 0:
#     digit = n%10

#     sum = sum + digit
#     n = n//10
# print("sum of digits is:", sum)


# n = int(input("enter a number:"))
# fact = 1
# for i in range(1, n+1):


arr = [1, 2, 3, 4, 5]
n = len(arr)
for i in range(n//2):
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
print("reversed array is:", arr)




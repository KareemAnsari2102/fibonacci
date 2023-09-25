# Creating a fibonacci program 
def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
num = int(input("enter any positive number: "))

if num < 0:
    print("input is not valid")

i = 0

print("fibonacci secession: ")

for i in range(0, num):
    print(fibonacci(i))
    
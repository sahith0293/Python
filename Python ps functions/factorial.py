def factorial(n):
    num =1
    while n>0:
        num = num * n
        n= n -1
    return num
    
        

num = int(input())
print(factorial(num))

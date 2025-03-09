def fib(n):
    a,b = 0,1
    sequence = []
    for i in range(0,n+1):
        sequence.append(a)
        
        a,b = b,a+b
        
    return sequence
        
        
        
num = int(input())     
print(fib(num))
        
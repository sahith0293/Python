numbers = [1,4,3,5,7]

def reverse(numbers):
    n = len(numbers)
    
    for i in range(n//2):
        numbers[i],numbers[n-i-1]=numbers[n-i-1],numbers[i]
    return numbers
        
    
    
    
res = reverse(numbers)
print(res)
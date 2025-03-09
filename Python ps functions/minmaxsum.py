numbers = [1,4,3,6,5,7]
def find_min_max(list):
    min = float('inf')
    max = float('-inf')
    total_sum  = 0
    for i in list:
        if i<min:
            min = i
        if i>max:
            max = i
        total_sum += i
    return min,max,total_sum;

res = find_min_max(numbers)
print(res)

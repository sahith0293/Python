# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
list = [1,4,3,5,8,7]
def rev_second_half(list):
    mid = len(list)//2
    low = mid
    high = len(list)-1
    while low<high:
        list[low],list[high] = list[high],list[low]
        low +=1
        high +=-1
    return list

res = rev_second_half(list)
print(list)


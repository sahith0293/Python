cmp1 = 5 + 3j
cmp2 = 6 - 5j
cmp3 = cmp1 + cmp2
print(cmp3)
print(cmp1-cmp2)
print(cmp1*cmp2)
print(cmp1/cmp2)
# print(cmp1//cmp2) floor divison wont work
# print(cmp1%cmp2) floor divison wont work
print(cmp1**cmp2)


# Boolean (True or False)
print(2<3)
print(2>=3)

bool1 = True
print(type(bool1))
print(type(False))

print(int(True)) 
print(int(False)) 

# sequences - List,Tuple,Strings,Range
#List - Collection of heterogenous elements which are indexable and list is mutable
list1 = [1,2,3,4,5,10,-1,'string1',True,[1,2,6]]
print(type(list1))
print(list1)
print(list1[4])
print(list1[5])
print(list1[9][2])
print(list1[len(list1)-1])
print(list1[-1])

#Slicing
print(list1[1:4])
print(list1[4:1:-1])
print(list1[2:8:2])
print(list1[-4:-2])
print(list1[-2:-5:-1])

temp = list1[9]
print(temp[2])
print(temp)

list1[-3]= "sahith"
print(list1)
list1[-3],list1[-1]="sahith kumar","koriginja"
# list1[-3:-5] = 4,5 does  not work
print(list1)


# Tuple -()- Immutable
tup1 = (1,2,True,"Str1",0.9)
print(tup1)
print(tup1[2:4])
print(tup1[-1:-4:-1])

# Tuple is faster than list

#range

print(list(range(0,100)))
print(list(range(100,0,-1)))
print(list(range(100,0,-2)))
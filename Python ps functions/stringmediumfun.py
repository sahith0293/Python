name = input()
def divide(name):
    if(len(name) %2 == 0):
        mid = len(name)//2
        part_1 = name[:mid]
        part_2 = name[mid:]
        
        return part_1,part_2
        
    else:
        return False
def checkVowels(part_1,part_2):
    vowels= "aeiouAEIOU"
    part1_count = 0
    part2_count = 0

    for i in part_1:
        if(i in vowels):
            part1_count += 1
        else:
            part1_count =0
    for i in part_2:
        if(i in vowels):
            part2_count += 2
        else:
            part2_count = 0
    if part1_count == part2_count:
        return True
    else:
        return False
    

result = divide(name)
if result:
    part_1,part_2 = result
    print(checkVowels(part_1,part_2))

else:
    print("False")



        


    
    
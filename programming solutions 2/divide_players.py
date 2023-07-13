skill = [3,2,5,1,3,4]

skill.sort()

start=0
end=len(skill)-1

target=skill[start]+skill[end]

print(skill,target)

total=0
while start<end:
    if skill[start]+skill[end]==target:
        total+=skill[start]*skill[end]
        start+=1
        end-=1
    else:
        break #return -1

print(total)
#return total
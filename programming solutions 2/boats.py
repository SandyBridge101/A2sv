people = [3,2,2,1]
limit = 3
people.sort()
start=0
end=len(people)-1

count=0

while start<=end:
    sum=people[start]+people[end]
    
    if sum>limit:
        end-=1
        count+=1
    elif sum<=limit:
        end-=1
        start+=1
        count+=1

print(count)
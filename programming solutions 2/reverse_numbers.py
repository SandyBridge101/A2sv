nums = [1,13,10,12,31]

for i in range(0,len(nums)):
    word=str(nums[i])
    tmp=[word[x] for x in range(len(word)-1,-1,-1)]
    print(''.join(tmp))
    nums.append(int(''.join(tmp)))
    
print(len(set(nums)))
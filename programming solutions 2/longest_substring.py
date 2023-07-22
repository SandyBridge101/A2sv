s = "dvdf"

p=0
start=1

curr_length=0
max_length=0

for i in range(start,len(s)+1):
    if len(set(s[p:i]))==len(s[p:i]):
        curr_length=len(s[p:i])
        max_length=max(curr_length,max_length)
    else:
        p+=1


print(max_length)
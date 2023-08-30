s = "abc"
shifts = [3,5,9]
answer=["_"]*(len(s))
x=0
answer[len(shifts)-1]=chr((ord(s[len(shifts)-1])-ord('a')+shifts[len(shifts)-1])%26+ord('a'))
for i in range(len(shifts)-2,-1,-1):
    shifts[i]+=shifts[i+1]
    answer[i]=chr((ord(s[i])-ord('a')+shifts[i])%26+ord('a'))

print(''.join(answer))
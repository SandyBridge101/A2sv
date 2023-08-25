
s = "abaababaa"
sample=[]

left=0

for right in range(0,int(len(s)/2)):
    curr=s[left:right+1]
    print(curr,"...")
    n=len(curr)-1
    is_sub=False
    for r in range(n,len(s),n+1):
        if len(s)%len(curr)!=0:break
        if len(s)==1:break
        print(list(s[r-n:r+1]))
        if s[r-n:r+1]==curr:
            is_sub=True
        else:
            is_sub=False
            break
    if is_sub==True:
        print(True)
        break

print(False)


piles =[9,8,7,6,5,1,2,3,4]
n=len(piles)
piles.sort()
p1=n-1
p2=n-2
p3=0

share=[]
my_share=0
#print(n,p1,p2,p3)

while p2-p3>=1:
    share=[piles[p1],piles[p2],piles[p3]]
    share.sort()
    my_share+=share[1]
    p1-=2
    p2-=2
    p3+=1
print(my_share)
piles =[9,8,7,6,5,1,2,3,4]
n=len(piles)
p1=n-1
p2=n-2
p3=n-3

share=[]
my_share=0
#print(n,p1,p2,p3)

while p3>=0:
    share=[piles[p1],piles[p2],piles[p3]]
    share.sort()
    my_share+=share[1]
    p1-=3
    p2-=3
    p3-=3
print(my_share)
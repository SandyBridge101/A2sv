from math import *
c = 2

start=0
end=int(sqrt(c))
print(start, end)
while start<=end:
    sum=(start*start)+(end*end)
    if sum==c:
        print(True)
        break
    if sum<c:start+=1
    if sum>c:end-=1
    
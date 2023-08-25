intervals =[[1,4],[0,2],[3,5]]

ans=[]
intervals.sort()
print("sorted",intervals)
if len(intervals)==1:
    print(intervals)
    #return intervals
for i in range(1,len(intervals)):
    print(intervals[i],intervals)
    
    if intervals[i][0]<=intervals[i-1][1]:
        #k=i+1
        print(intervals[i][0],intervals[i-1][1])
        intervals[i]=[min(intervals[i-1][0],intervals[i][0]),max(intervals[i][1],intervals[i-1][1])]
        intervals[i-1]=None
        
    
ans=[i for i in intervals if i!=None]
print(ans,intervals)
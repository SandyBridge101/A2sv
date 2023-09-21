class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        self.persons=persons
        self.n=len(persons)
        self.max_arr=[]
        self.seen={} 
        self.seen[self.persons[0]]=1+self.seen.get(self.persons[0],0)
        self.curr_max=self.persons[0]
        self.max_arr.append(self.curr_max)
        for i in range(1,self.n):
            self.seen[self.persons[i]]=1+self.seen.get(self.persons[i],0)
            if self.seen[self.persons[i]]>=self.seen[self.curr_max]:
                self.curr_max=self.persons[i]
            self.max_arr.append(self.curr_max)

    def q(self, t: int) -> int:
        pos=self.n-1
        low,high=0,self.n-1
        while low<=high:
            mid=low+(high-low)//2
            #print(mid)
            if self.times[mid]<=t:
                pos=mid
                low=mid+1
            else:
                high=mid-1
        return self.max_arr[pos]
                

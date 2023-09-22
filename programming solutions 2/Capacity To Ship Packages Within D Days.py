class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        n=len(weights)
        low,high=max(weights),sum(weights)
        cap=0

        def days_per_given_capacity(capacity,n):
            days=0
            count=0
            for i in range(n):
                count+=weights[i]
                if count>capacity:
                    days+=1
                    count=weights[i]
            if count<=capacity:
                days+=1
            return days

        while low<=high:
            mid=low+(high-low)//2
            number_of_days=days_per_given_capacity(mid,n)

            if number_of_days>days:
                low=mid+1
            else:
                cap=mid
                high=mid-1
        return cap

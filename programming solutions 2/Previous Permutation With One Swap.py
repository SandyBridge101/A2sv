class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]: 
        n=len(arr)
        mx1,mx2=-1,-1
        mr=-1

        for i in range(n-1,-1,-1):
            mx=-1
            x=-1
            for j in range(n-1,i,-1):
                if arr[j]>=mx and arr[j]<arr[i]:
                    mx=arr[j]
                    x=j
            if x!=-1:
                arr[x],arr[i]=arr[i],arr[x]
                break
                  
        return arr 

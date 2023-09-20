class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        temp=0
        print(l,r)

        def rev(l,r):
            if l>=r:
                return
            else:
                #print(l,r)
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
                r-=1
                l+=1

                rev(l,r)
        rev(l,r)

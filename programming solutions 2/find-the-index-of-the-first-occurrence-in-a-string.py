class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        j=0
        i=0
        f=0

        while i<len(haystack):
            print(i,j)
            if j==len(needle):
                return i-len(needle)
            if haystack[i]==needle[j]:
                if j==0:
                    f=i
                j+=1
                i+=1
            else:
                i=f+1
                f+=1
                j=0
            if j==len(needle):
                return i-len(needle)
            

        return -1

        
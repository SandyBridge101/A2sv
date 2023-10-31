class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        
        for a in s:
            print(a)
            if not stack:
                stack.append([a,1])
                continue
            if stack[-1][0]==a:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([a,1])
        return "".join([st[0]*st[1] for st in stack])

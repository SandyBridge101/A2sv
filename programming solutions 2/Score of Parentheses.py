class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        n=len(s)
        score=0
        closed=0
        for i in range(n):
            if not stack:
                stack.append(s[i])
            elif s[i]=='(':
                stack.append(s[i])
                print(closed)
                closed=0
            elif s[i]==')' and stack[-1]=='(':
                score+=1
                closed+=1
                stack.pop()

        print(stack,score,closed)
        return 0

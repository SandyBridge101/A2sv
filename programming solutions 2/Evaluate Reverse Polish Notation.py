class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n=len(tokens)
        stack=[]

        for i in range(n):
            if tokens[i]!='+' and tokens[i]!='-' and tokens[i]!='/' and tokens[i]!='*':
                stack.append(tokens[i])
            else:
                a=stack.pop()
                b=stack.pop()
                if tokens[i]=='+':
                    stack.append(int(a)+int(b))
                elif tokens[i]=='-':
                    stack.append(int(b)-int(a))
                elif tokens[i]=='/':
                    stack.append(int(b)/int(a))
                elif tokens[i]=='*':
                    stack.append(int(a)*int(b))
                print(a,b)
        #print(stack)
        return int(stack[-1])

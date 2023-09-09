class Solution:
    def simplifyPath(self, path: str) -> str:
        split_path=path.split('/')
        answer=[]
        print(split_path)
        for i in range(0,len(split_path)):
            if split_path[i]=='.' or split_path[i]=='':
                continue
            elif split_path[i]=='..':
                if answer:
                    answer.pop()
            else:
                answer.append(split_path[i])

        output=""
        #print(answer)

        for word in answer:
            output=output+"/"+word

        if output:
            return output
        else:
            return "/"
        

        

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer=[]
        for i in range(0,len(A)):
            sub_a=A[0:i+1]
            sub_b=B[0:i+1]
            
            inter=set(sub_a).intersection(set(sub_b))
            print(sub_a,sub_b,inter)
            answer.append(len(inter))
        return answer

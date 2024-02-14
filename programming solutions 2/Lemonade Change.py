class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes=defaultdict(int)
        changes=defaultdict(int)
        x=0
        for bill in bills:
            x+=1
            print(x,notes)
            notes[bill]+=1
            change=bill-5
            if change==15:
                if (notes[5]>0 and notes[10]>0):
                    notes[5]-=1
                    notes[10]-=1
                elif (notes[10]<=0 and notes[5]>=3):
                    notes[5]-=3
                else:
                    return False
                    
            elif change==5:
                if notes[5]<=0:
                    print(change,notes)
                    return False
                notes[5]-=1
        
        return True
       

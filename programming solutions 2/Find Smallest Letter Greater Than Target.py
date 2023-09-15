class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        mx=0

        while low <= high:
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid -1 
            
            elif letters[mid] < target:
                low = mid + 1
            
            elif letters[mid] == target:
                return letters[mid + 1]

            else:
                return letters[mid]

                
        if mx:
            return mx
        return letters[0]
        
        #Using linear search
        # for letter in letters:
        #     if letter > target:
        #         return letter
        
        # return letters[0]


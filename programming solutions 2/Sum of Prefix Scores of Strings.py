class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}


class Solution:
    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        curr=self.root
        for s in word:
            if s not in curr.children:
                curr.children[s]=TrieNode()    
            curr.children[s].count+=1
            curr=curr.children[s]
        

    def search(self, word: str) -> bool:
        curr=self.root
        c=0
        for s in word:
            c+=curr.children[s].count
            curr=curr.children[s]

        return c

        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        n=len(words)
        res=[]
        for w in words:
            self.insert(w)
    
        for w in words:
            res.append(self.search(w))

        return res

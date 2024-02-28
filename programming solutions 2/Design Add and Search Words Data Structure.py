class TrieNode:
    def __init__(self):
        self.is_end=False
        self.children=defaultdict(TrieNode)

    
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    
    def addWord(self, word: str) -> None:
        curr=self.root
        for s in word:
            if curr.children[s]==None:
                curr.children[s]=TrieNode()
            curr=curr.children[s]
        curr.is_end=True
        

    def search(self, word: str) -> bool:
        curr=self.root
        m=len(word)
        print('s')

        def func(i,curr):
        
            if i>=m:
                return curr.is_end

            
            if word[i]=='.':
                res=False
                for c in curr.children:
                    res=res or (func(i+1,curr.children[c]) and curr.children[c]!=None)
                return res
            else:
                if curr.children[word[i]]==None:
                    return False
                else:
                    return func(i+1,curr.children[word[i]])

        



        return func(0,curr)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

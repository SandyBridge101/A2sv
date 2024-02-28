class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for s in word:
            if curr.children[ord(s)-ord('a')]==None:
                curr.children[ord(s)-ord('a')]=TrieNode()    
            curr=curr.children[ord(s)-ord('a')]
        curr.is_end=True
        

    def search(self, word: str) -> bool:
        curr=self.root
        for s in word:
            if curr.children[ord(s)-ord('a')]==None:
                return False
            else:
                curr=curr.children[ord(s)-ord('a')]

        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for s in prefix:
            if curr.children[ord(s)-ord('a')]==None:
                print(s)
                return False
            else:
                curr=curr.children[ord(s)-ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
word='apple'
prefix='a'
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)

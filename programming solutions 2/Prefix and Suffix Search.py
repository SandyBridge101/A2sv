class TrieNode:
    def __init__(self):
        self.index = 0
        self.children = {}


class WordFilter:
    def __init__(self, words: List[str]):
        self.root=  TrieNode()
        for idx, word in enumerate(words):
            word=word + '#'
            length=len(word)
            word+=word
            
            for i in range(length):
                curr=self.root
                curr.index=idx 
                for c in word[i:]:
                    if c not in curr.children:
                        curr.children[c]=TrieNode()
                    curr=curr.children[c]                  
                    curr.index=idx
            


    def f(self, pref: str, suff: str) -> int:
        curr=self.root
        #print(curr.children)
        for s in suff+'#'+pref:
            if s not in curr.children:
                return -1   
            curr=curr.children[s]
        return curr.index

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        class TrieNode:
            def __init__(self):
                self.is_end = False
                self.children = defaultdict(TrieNode)

        class Trie:

            def __init__(self):
                self.root=TrieNode()
                

            def insert(self, word: str) -> None:
                curr=self.root
                for s in word:
                    if curr.children[s]==None:
                        curr.children[s]=TrieNode()    
                    curr=curr.children[s]
                curr.is_end=True
                

            def search(self, word: str) -> bool:
                curr=self.root

                def func(curr):

                    if curr.is_end==True:
                        return ''

                    if len(curr.children)!=1:
                        return ''


                    x=list(curr.children.keys())[0]
                    return x+func(curr.children[x])

                return func(curr)
                
                
        if "" in strs:
            return ""
                
        obj = Trie()
        for word in strs:
            obj.insert(word)
        param = obj.search(word)

        return param

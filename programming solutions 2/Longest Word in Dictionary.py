class Solution:
    def longestWord(self, words: List[str]) -> str:
        n=len(words)
        count=defaultdict(int)
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
                c=0
                curr=self.root
                #print('---------------')
                for s in word:
                    if curr.children[s].is_end==True:
                        c+=1
                    if curr.is_end==False and curr!=self.root:
                        break     
                    if not curr.children:
                        break
                    #print(s,c,curr.children[s].is_end,'========')
 
                    x=ord(s)-ord('a')
                    curr=curr.children[s]

                return c

                
                
                
        obj = Trie()
        for word in words:
            obj.insert(word)
        

        for word in words:
            count[word]=obj.search(word)

        print(count)
        mx=-1

        mv=''

        for c in sorted(count.keys()):
            if count[c]>mx and len(c)==count[c]:
                mx=count[c]
                mv=c

        return mv

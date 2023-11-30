"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_count=0
        vs=set()
        def dfs(node,count):
            if not node:
                return
            print(node.val)
            count+=1
            vs.add(count)
            for child in node.children:
                dfs(child,count)
        
        dfs(root,0)
        
        return len(vs)
        

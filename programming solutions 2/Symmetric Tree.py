# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left=[]
        right=[]
        
        def symmetric(l,r):
            if not r and not l:
                return True
            r_value=0
            l_value=0
            if not r:
                r_value=None
                l_value=l.val
            elif not l:
                r_value=r.val
                l_value=None
            else:
                r_value=r.val
                l_value=l.val
                

            if r_value!=l_value:
                #print(r,l)
                return False

            return symmetric(r.left,l.right) and symmetric(l.left,r.right)

            
        
        
        return (symmetric(root.left,root.right))

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        
        dummy=TreeNode()
        if not root1:
            dummy.val=0+root2.val
            dummy.left=self.mergeTrees(None,root2.left)
            dummy.right=self.mergeTrees(None,root2.right)
        elif not root2:
            dummy.val=root1.val+0
            dummy.left=self.mergeTrees(root1.left,None)
            dummy.right=self.mergeTrees(root1.right,None)
        else:
            dummy.val=root1.val+root2.val
            dummy.left=self.mergeTrees(root1.left,root2.left)
            dummy.right=self.mergeTrees(root1.right,root2.right)

        return dummy

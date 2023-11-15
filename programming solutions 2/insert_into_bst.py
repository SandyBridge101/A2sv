# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent=root
        def insert(root):
            if not root:
                root=TreeNode(val)
                return
            if val<root.val:
                if not root.left:
                    root.left=TreeNode(val)
                    return
                insert(root.left)
            else:     
                if not root.right:
                    root.right=TreeNode(val)
                    return
                insert(root.right)
        if not root:
            root=TreeNode(val)
        else:
            insert(root)
        return root
        

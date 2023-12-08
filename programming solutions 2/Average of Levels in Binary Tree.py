# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def bfs(node):
            queue=deque()
            avg=deque()
            queue.append(node)


            while queue:
                l=len(queue)
                total=0

                for _ in range(l):
                    q=queue.popleft()
                    total+=q.val
                    if q.left:
                        queue.append(q.left)
                    if q.right:
                        queue.append(q.right)

                avg.append(total/l)
            return avg
        return bfs(root)




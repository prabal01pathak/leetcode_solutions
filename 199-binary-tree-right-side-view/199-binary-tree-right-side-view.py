from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([ root ])
        res = []
        while queue:
            res.append(queue[-1].val)
            queue = self.get_nodes(queue)
        return res
    
    def get_nodes(self, queue):
        res = deque([])
        for i in queue:
            if i.left:
                res.append(i.left)
            if i.right:
                res.append(i.right)
        return res
        
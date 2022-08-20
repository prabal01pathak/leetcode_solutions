from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative version
        if root is None:
            return 0
        queue = deque([ root ])
        no_of_level = 1
        l = 0
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            no_of_level -= 1
            if no_of_level == 0:
                l += 1
                no_of_level = len(queue)
        return l
        
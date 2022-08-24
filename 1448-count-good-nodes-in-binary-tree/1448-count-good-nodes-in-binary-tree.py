# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def get_max(node, max_val):
            if not node:
                return None
            if node.val >= max_val:
                max_val = node.val
                self.res += 1
            get_max(node.right, max_val)
            get_max(node.left, max_val)
            
        max_val = float("-inf")
        self.res = 0
        get_max(root, max_val)
        return self.res
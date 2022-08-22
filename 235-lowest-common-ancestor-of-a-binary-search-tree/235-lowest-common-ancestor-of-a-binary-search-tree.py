# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p, q = min(p.val, q.val), max(p.val, q.val)
        self.n = None
        def helper(node):
            if not node:
                return None
            if p <= node.val <=q and self.n is None:
                self.n = node
                return node
            helper(node.left)
            helper(node.right)
        helper(root)
        return self.n
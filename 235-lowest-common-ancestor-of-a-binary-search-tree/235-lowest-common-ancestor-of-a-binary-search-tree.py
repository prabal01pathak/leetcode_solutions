# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [ root ]
        p, q = min(p.val, q.val), max(p.val, q.val)
        while stack:
            node = stack.pop()
            if p <= node.val <= q:
                return node
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return node
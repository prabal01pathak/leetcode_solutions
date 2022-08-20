# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], value=0) -> int:
        self.ans = 0
        def helper(node):
            if node is None:
                return -1
            left, right = helper(node.left), helper(node.right)
            self.ans = max(self.ans , 2+left + right)
            return 1+max(left, right)
        helper(root)
        return self.ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True
        def getHeight(node):
            if node is None:
                return 0
            left, right = getHeight(node.left), getHeight(node.right)
            if abs(left - right) > 1:
                self.bal = False
            return 1 + max(left, right)
        getHeight(root)
        return self.bal
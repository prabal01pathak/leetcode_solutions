# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if root.val == subRoot.val:
            if self.checkSubtree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def checkSubtree(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        if (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False
        if root.val == subRoot.val:
            return (self.checkSubtree(root.left, subRoot.left) and
                    self.checkSubtree(root.right, subRoot.right))
        return False
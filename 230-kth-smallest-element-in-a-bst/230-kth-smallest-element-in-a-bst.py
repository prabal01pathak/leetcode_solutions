# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def traverseTree(node):
            if not node:
                return None
            traverseTree(node.left)
            view.append(node.val)
            traverseTree(node.right)
            
        view = []
        traverseTree(root)
        return view[k-1]
        
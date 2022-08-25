# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [ root ]
        node = root
        v = 0
        while stack:
            if node and  node.left:
                node = node.left
                stack.append(node)
            else:
                node = stack.pop()
                v += 1
                if v == k:
                    return node.val
                if node.right:
                    node = node.right
                    stack.append(node)
                else:
                    node = None

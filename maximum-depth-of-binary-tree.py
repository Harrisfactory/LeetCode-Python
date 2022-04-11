# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)
        if left_count > right_count:
            return left_count+1
        else: return right_count+1
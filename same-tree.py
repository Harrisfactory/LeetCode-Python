# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #if both trees are empty we can return True
        if p == None and q == None:
            return True
        
        #if both trees are not empty we must compare and move
        elif p and q:
            if (p.val == q.val) and (self.isSameTree(p.left,q.left)) and (self.isSameTree(p.right,q.right)):
                return True
        
        #else one tree is not empty so we return False
        else:
            return False


        #solution is likely O(m) where m < n since smallest tree will cause us to stop iterating
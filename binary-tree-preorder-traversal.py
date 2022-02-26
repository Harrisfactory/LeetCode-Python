# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        preorder_list = []
        
        #if there is a root, add to list
        if root:     
            preorder_list.append(root.val)
            #if there is a left root, add to list
            if root.left:
                preorder_list = preorder_list + self.preorderTraversal(root.left)
            #if there is a right roog, add to list
            if root.right:
                preorder_list = preorder_list + self.preorderTraversal(root.right)
        return preorder_list
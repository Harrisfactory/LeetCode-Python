# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        inorder_list = []
        
        if root:     
            #if there is a left root, add to list
            if root.left: 
                inorder_list = inorder_list + self.inorderTraversal(root.left)
            inorder_list.append(root.val)
            #if there is a right root, add to list
            if root.right:
                inorder_list = inorder_list + self.inorderTraversal(root.right)
        return inorder_list
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        postorder_list = []
        
        #if we have a root node
        if root:
            
            postorder_list = postorder_list + self.postorderTraversal(root.left)
            postorder_list = postorder_list + self.postorderTraversal(root.right)
            postorder_list.append(root.val)
            
        return postorder_list
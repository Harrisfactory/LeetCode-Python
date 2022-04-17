# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        #array that will capture the inorder traversal of the binary search tree
        rearranged_tree = []
        
        #recursivly capture inorder traversal
        def inorder(root):
            
            if root == None:
                return 
                
            inorder(root.left)
            rearranged_tree.append(root.val)
            inorder(root.right)
            print(rearranged_tree)
           
        inorder(root)
    
        #set initial root of new slanted tree
        new_root = TreeNode(rearranged_tree[0])
        #init temp to retain new root
        temp = new_root
        #have root so start at next node
        for i in range(1, len(rearranged_tree)):
            #build only to the right
            temp.right = TreeNode(rearranged_tree[i])
            temp = temp.right
        
        return new_root
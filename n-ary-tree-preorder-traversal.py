"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        preorder_list = []
        
        def dfs(root):
            
            if not root: return
            
            preorder_list.append(root.val)
            for child in root.children:
                dfs(child)
                
        dfs(root)
        
        return preorder_list
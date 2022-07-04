# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #base case
        if root is None:
            return
        #setup queue
        queue = []
        queue.append(root)
        #list that will hold our levels
        result_list = []
        #while still on levels
        while len(queue) > 0:
            #add values to local list at each level
            current_level = []

            for i in range(0, len(queue)):
                #remove current node from queue to process
                node = queue.pop(0)
                #add current nodes value to current level
                current_level.append(node.val)
                #place left and right nodes into queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #local list has values so we can append to larger list
            if current_level:
                result_list.append(current_level)

        return result_list

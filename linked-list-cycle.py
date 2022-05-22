# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #store each node in dict and check if any are reached a 2nd time
        
        stored_nodes = {}

        while head != None:
            if head in stored_nodes:
                return True
            else:
                stored_nodes[head] = 1
            
            head = head.next
            
        return False
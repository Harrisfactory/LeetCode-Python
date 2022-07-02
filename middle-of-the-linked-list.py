# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        linked_count = 0
        
        cur_count = 0
        
        old = head
        
        #get count of linked list
        while head:
            
            linked_count +=1
            
            head = head.next
        
        #comare counts middle with current count
        while old:
            if cur_count == (linked_count // 2):
                return old
            
            cur_count+=1
            
            old = old.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #we want to keep a running the total of the curr consecutive numbers
        
        #if next head is 0 we want to insert those numbers to a new Node
        
        merged_list = LinkedList()
        merged_list.head = ListNode(None)
        
        merged_head = merged_list.head 
        running_total = 0
        
        while head.next is not None:
            
            next_node = head.next
            running_total += head.val
            if next_node.val is 0:
                merged_list.head.next = ListNode(running_total)
                merged_list.head = merged_list.head.next
                running_total = 0
            
            head = head.next
        
        #removing dummy data at the head
        merged_head = merged_head.next
       
        return merged_head
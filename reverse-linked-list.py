# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        rev = None
        
        #while still on node point current head val to previous head val
        #rev = None <- 1 <- 2 <- 3 <- 4 <- 5
        while head:
            rev = ListNode(head.val, rev)
            head = head.next
        return rev
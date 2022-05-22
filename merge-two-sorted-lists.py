# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        sorted_list = ListNode('')

        head = sorted_list

        if not list1 and not list2:
            return ListNode('')

        while list1 != None or list2 != None:
            if list1:
                if list2 != None and list1.val <= list2.val:
                    sorted_list.val = list1.val
                    sorted_list.next = ListNode('')
                    sorted_list = sorted_list.next
                    list1 = list1.next
                elif list2 == None and list1 != None:
                    sorted_list.val = list1.val
                    if list1.next != None:
                        sorted_list.next = ListNode('')
                    sorted_list = sorted_list.next
                    list1 = list1.next
            if list2:
                if list1 != None and list2.val <= list1.val:
                    sorted_list.val = list2.val
                    sorted_list.next = ListNode('')
                    sorted_list = sorted_list.next
                    list2 = list2.next
                elif list1 == None and list2 != None:
                    sorted_list.val = list2.val
                    if list2.next != None:
                        sorted_list.next = ListNode('')
                    sorted_list = sorted_list.next
                    list2 = list2.next

        return head

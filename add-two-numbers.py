# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #arr append: check
        
        #reverse iterate append to string:
        
        #string to int:
        
        #set to two corrosponding nums
        
        #add nums
        
        #int to str
        
        #explode to arr
        
        #set each element to Node
        
        #set pointers connecting nodes to linked list then return
        
        num_one_arr = []
        
        num_two_arr = []
        
        num_one = ""
        
        num_two = ""
        
        while l1 is not None:
            num_one_arr.append(l1.val)
            
            l1 = l1.next
        while l2 is not None:
            num_two_arr.append(l2.val)
            
            l2 = l2.next
            
            
        for i in reversed(num_one_arr):
            num_one = num_one + str(i)
        for i in reversed(num_two_arr):
            num_two = num_two + str(i)
            
            
        ans_num = list(str(int(num_one) + int(num_two)))
        
        rev_ans_num = []
        
        for i in reversed(ans_num):
            rev_ans_num.append(i)

        head = ListNode(rev_ans_num[0])
        
        start_node = head
      
        for i in range(1, len(rev_ans_num)):
            head.next = ListNode(rev_ans_num[i])
            
            head = head.next
        
        return start_node
        
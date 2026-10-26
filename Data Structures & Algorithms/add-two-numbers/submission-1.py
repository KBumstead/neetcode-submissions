# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total1, total2 = 0, 0
        mult1, mult2 = 1,1
        while l1:
            total1 += (l1.val * mult1)
            mult1 *= 10
            l1 = l1.next

        while l2:
            total2 += (l2.val * mult2)
            mult2 *= 10
            l2 = l2.next
        
        total = total1+total2

        if total == 0:
            return ListNode(0)

        dummy = ListNode(0)
        res = dummy

        

        while total  > 0 :
            temp = total % 10 
            res.next = ListNode(temp)
            res = res.next
            total = total //  10



       
        return dummy.next




        
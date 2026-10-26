# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev, curr = None, second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
                    
        rev = prev

        first = head

        while rev:
            tmp1 = first.next
            tmp2 = rev.next
            first.next = rev
            rev.next = tmp1
            first = tmp1
            rev = tmp2



            

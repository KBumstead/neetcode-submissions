# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        arr = []
        temp = head

        while temp:
            arr.append(temp)
            temp = temp.next

        index = len(arr) - n
        if index == 0:
            return head.next

        arr[index - 1].next = arr[index].next

        return head

            
        
        
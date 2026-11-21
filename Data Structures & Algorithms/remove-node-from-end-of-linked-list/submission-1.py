# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            
            return None
        count = 1
        current = head
        while current.next is not None:
            count += 1
            current = current.next
        
        target = count - n + 1
        count = 1
        if target == 1:
            return head.next
        current = head
        while count != target -1:
            current = current.next
            count += 1
        current.next = current.next.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current_fast = head
        current = head
        while True:
            if current_fast is None:
                break
            current = current.next
            current_fast = current_fast.next
            if current_fast is None:
                break
            current_fast = current_fast.next
            if current_fast is current:
                return True
        return False
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        current = head
        while True:
            if current is None:
                break
            if visited.get(current):
                return True 
            visited[current] = 1
            current = current.next
        return False
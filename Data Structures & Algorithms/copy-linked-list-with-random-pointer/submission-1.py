"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        pairs = {}
        new_head = Node(head.val)
        current = head.next
        new_current = new_head
        pairs[head] = new_head
        while current is not None:
            temp = Node(current.val)
            new_current.next = temp
            pairs[current] = new_current.next
            new_current = new_current.next
            current = current.next
        current = head
        new_current = new_head
        while current is not None:
            new_current.random = pairs.get(current.random)
            current = current.next
            new_current = new_current.next
        return new_head
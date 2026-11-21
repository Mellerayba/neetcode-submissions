class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return


        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        second = slow.next
        slow.next = None
        previous = None
        while second:
            temp = second.next
            second.next = previous
            previous = second
            second = temp


        first, second = head, previous
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
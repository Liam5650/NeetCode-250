from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Get the midpoint, slow will be the last val in sectioned lists
        slow, fast = head, head.next      # type: ignore
        while fast and fast.next:
            slow = slow.next      # type: ignore
            fast = fast.next.next

        # Separate the lists
        head2 = slow.next      # type: ignore
        slow.next = None      # type: ignore

        # Reverse the second list
        prev = None
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        # Reassign for clarity
        head2 = prev

        # Append to dummy node
        dummy = tail = ListNode()
        while head and head2:

            # Left half
            tail.next = head
            tail = tail.next
            head = head.next

            # Right half
            tail.next = head2
            tail = tail.next
            head2 = head2.next

        # Make sure no vals left because of uneven list sectioning (ex if length 5)
        if head: tail.next = head
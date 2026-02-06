from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initial state for the end of the first node
        prev = None

        # While we havent reached the end of the list (still a valid node to process)
        while head:

            # Temporarily store the next node in the list
            temp = head.next

            # Flip current node
            head.next = prev

            # Set the current node as the previous  (we just processed it)
            prev = head

            # Start again from the next node in the list
            head = temp

        # Prev will be the last node that was processed
        return prev
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:\
    
        # Use a dummy node for easy insertion and tracking the head of list
        tail = dummy = ListNode()

        # Heads of each list
        h1 = list1
        h2 = list2

        while h1 and h2:
            
            # Attatch the correct node to the tail and advance
            if h1.val > h2.val:
                tail.next = h2
                h2 = h2.next
            else:
                tail.next = h1
                h1 = h1.next

            tail = tail.next

        # Make sure nothing else remains in either list. Attach
        if h1: tail.next = h1
        elif h2: tail.next = h2

        return dummy.next
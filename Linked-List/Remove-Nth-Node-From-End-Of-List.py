from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Do a two-pass to get the length of the list, then navigate to the node
        # that needs to be removed

        # Get length of list
        length_list = 0 
        node = head # Use a reference for the name so "head" still points to the start
        while node:
            length_list += 1
            node = node.next

        # Navigate to the node, keeping track of the prev to make linking easy
        prev = None
        node = head
        for _ in range(length_list - n):
            prev = node
            node = node.next # type: ignore

        # There are four cases at first glance - removing the only node, and then 
        # one of either removing the node at the start, middle, or end

        # Only one node and the start are technicaly the same case,
        # since node.next covers returning both None or the next node
        if prev == None:
            return node.next # type: ignore
        
        # Same as removing in the middle or at end, as this 
        # correctly updates the prev to either None (if at end)
        # or the node that follows 
        else:
            prev.next = node.next # type: ignore
            return head
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Use two pointers to "build" the list index by index in place.
        # The left index represents the current position that the list is
        # sorted until with unique values. We can then use a right pointer
        # and iterate through, skipping values equal to the last position
        # we have validated. 
        l = 0 
        r = 1

        while r < len(nums):
            
            # If pointing to equal values, keep advancing the right pointer.
            if nums[l] == nums[r]:
                r += 1

            # We have found a new value (if within bounds still). Move our
            # left pointer to the next position to place the new value.
            elif r < len(nums):
                l += 1
                nums[l] = nums[r]
        
        # The left pointer (0 indexed so add one) shows how many values 
        # were unique. Therefore, we can simply pop off the rest that were
        # not part of the sorted unique sublist.
        valid = l + 1
        for i in range(len(nums) - valid): nums.pop()
        return valid
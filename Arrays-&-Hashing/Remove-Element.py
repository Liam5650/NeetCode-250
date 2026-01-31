from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # We basically want to move all values to the start of the 
        # list that are valid. To do this, we can simply use a pointer
        # to mark the ending spot of the "validated" list. Then
        # we simply iterate through, swapping valid nums to the pointer
        # and incrementing, and skipping invalid. 

        # The reason this works is that we know for sure that all values
        # before the one we have reached have already been processed and 
        # moved within the valid k range, so we dont have to worry about 
        # overwriting anything outside of it (i.e., before the current
        # index but after the k index, as these have been processed
        # already and can be safetly overwritten).

        k = 0
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[k] = nums[i]
                k += 1

        return k
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Simple binary search, check middle val then split list in half
        # based on higher or lower

        l, r = 0, len(nums) - 1
        index = 0

        while l <= r:
            index = ((r - l) // 2) + l
            guess = nums[index]
            if guess == target: return index
            elif guess > target: 
                r = index - 1
            else: l = index + 1
        
        # If we got through this point, check if the number should have been
        # inserted at this point (if smaller than the val at the index) or at
        # the next (if bigger)
        return index + 1 if nums[index] < target else index
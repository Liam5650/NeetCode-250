from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Use two pointers to track the search area in the list
        l = 0
        r = len(nums) - 1

        # Wait for them to cross or be equal (meaning search has been exhausted)
        while l <= r:

            # Choose mid point
            index = (r-l//2) + l
            guess = nums[index]

            # Check if we hit the target, otherwise shrink search area
            if guess == target: return index
            elif guess > target: r = index - 1
            else: l = index + 1

        return -1
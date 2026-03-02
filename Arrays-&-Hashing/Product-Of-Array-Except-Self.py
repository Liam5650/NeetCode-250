from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Base case
        if len(nums) <= 1: return nums

        # Suppose we have a list [A, B, C, D]. We are looking for the following
        # values: [B*C*D, A*C*D, A*B*D, A*B*C]. Notice how each section is what
        # the prodcuct of what comes before and what comes after. We can precompute 
        # the values before and after by doing two passes through the original array.

        # This will compute [A, A*B, A*B*C, A*B*C*D]
        before = []
        for i in range(len(nums)):
            if before == []: before.append(nums[i])
            else: before.append(nums[i] * before[-1])

        # This will compute [A*B*C*D, B*C*D, C*D, D]
        after = []
        for i in range(len(nums) - 1, -1, -1):
            if after == []: after.append(nums[i])
            else: after.append(nums[i] * after[-1])
        after.reverse()

        # We now have everything we need. Notice for each index, all we need is 
        # the product of the index to the left in the "before" array and the 
        # index to the right in the "after" array.

        # Compute the first and last values for simplicity and not worrying about
        # staying in bounds
        first = after[1]
        last = before[-2]

        # Compute the middle values
        middle = []
        for i in range(1, len(nums) - 1, 1):
            middle.append(before[i-1] * after[i+1])

        # Combine
        return [first] + middle + [last]
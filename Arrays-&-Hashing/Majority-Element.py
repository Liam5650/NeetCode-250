from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # Get counts of all numbers, while checking if it is 
        # the greatest seen. Use dict for fast lookups and
        counts = {}
        max_key = nums[0]

        for num in nums:
            if num in counts: 
                counts[num] += 1
                if counts[num] > counts[max_key]: max_key = num

            else: counts[num] = 1

        return max_key
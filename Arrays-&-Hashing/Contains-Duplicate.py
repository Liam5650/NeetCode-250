from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Iterate through list while storing seen vals in set,
        # checking if they have been seen before (O(1) lookup due
        # to using set)

        seen = set()

        for num in nums:
            if num in seen: return True
            else:
                seen.add(num)
        
        # If we iterate through the whole list, all vals were unique
        return False
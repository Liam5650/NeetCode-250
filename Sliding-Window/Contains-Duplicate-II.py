from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # Simply iterate through using a dictionary storing seen vals
        # and the index it was seen at. Check when we find equal vals

        seen = {}

        for i, num in enumerate(nums):
            
            # Add unseen nums
            if not num in seen:
                seen[num] = i
            
            # If it has been seen, check the condition 
            elif i - seen[num] <= k:
                return True
            
            # Otherwise update the index to the latest, as this will make 
            # sure the window stays the smallest if there ends up being another
            # equal val to check
            else: seen[num] = i

        return False
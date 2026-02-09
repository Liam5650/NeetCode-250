from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # The values in the list are limited, i.e. only 0-2. This
        # is a classic example where we can use bucket sort

        counts = [0]*3

        for num in nums:
            counts[num] += 1

        appended = 0
        i = 0
        j = 0
        while i < len(nums):
            while appended < counts[j]:
                nums[i] = counts[j]
                appended += 1
                i +=1
            
            appended = 0
            i += 1
            j += 1
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Simple algo, we create a dictionary with seen values matched
        # to their index. When processing a new num in nums, we see if
        # its complement (comp + num = target) exists in the dict, otherwise
        # we can just append the current val. 

        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen: return [seen[complement], i]
            else: seen[nums[i]] = i

        return []
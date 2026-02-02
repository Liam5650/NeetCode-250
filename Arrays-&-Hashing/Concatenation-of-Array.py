from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        # This can simply be achieved by creating a new list
        # that contains two copies of the first

        # Create the ans list
        ans = []

        # Copy nums list twice
        for i in range(2):
            for num in nums:
                ans.append(num)

        return ans
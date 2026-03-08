from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # First we convert the list to a set. Then, find the start of "chains", 
        # which are simply vals with nothing that is 1 lower. Then, see how long
        # the chain goes. Each of these is an O(n) operation, with O(n) space

        # Base case
        if len(nums) < 2: return len(nums)

        # Get the chains in the list
        seen = set(nums)
        chains = []
        for num in seen:
            if not (num - 1 in seen): chains.append (num)
        
        # Explore each to find the longest and return
        longest = 1 
        for chain_head in chains:
            curr_length = 1
            while chain_head + 1 in seen:
                chain_head += 1
                curr_length += 1
            
            if curr_length > longest: longest = curr_length
        
        return longest
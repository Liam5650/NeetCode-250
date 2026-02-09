from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # The most number of the same element we can have is constrained
        # by the size of the nums list (n). Thus, we can create n buckets
        # and sort the numbers based on this

        # Create a bucket for each possible count from 0 (kept just for
        # easy indexing) to len of the nums list
        buckets = [[] for i in range(len(nums) + 1)]

        # Get the count for each num in the list
        counts = {}
        for num in nums:
            if num in counts: counts[num] += 1
            else: counts[num] = 1

        # Place each num in the correct bucket
        for key in counts:
            buckets[counts[key]].append(key)

        # Build the output based on how many vals we want
        res = []

        # Start from back (highest frequency in nums)
        i = len(buckets)-1

        # Go through until we have the num of vals we want
        while k > 0:

            # Go through a bucket until it is empty, then move on to next
            if buckets[i] != []: 
                res.append(buckets[i].pop())
                k -= 1
            else: i -= 1

        return res
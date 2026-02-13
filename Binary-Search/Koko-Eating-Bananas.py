from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        sp_min = len(piles) // h
        sp_max = max(piles)
        min_time = -1

        while sp_min <= sp_max:
            guess = ((sp_max - sp_min) // 2) + sp_min
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / guess)

            if time <= h:
                if min_time == -1 or time < min_time:
                    min_time = time
                sp_max = guess - 1

            else:
                sp_min = guess + 1
            
        return min_time

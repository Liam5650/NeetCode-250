from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Max profit doing nothing is 0, we don't want to go negative
        max_p = 0

        # Use a sliding window to search the list of prices. If
        # a range has negative value, we can simply move the window to
        # start searching the next range.

        l = 0
        r = 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                if profit > max_p: max_p = profit
                r += 1
            else:
                l = r
                r += 1

        return max_p
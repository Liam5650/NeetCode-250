# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # Simple binary search, guess the middle number to segment
        # the search number in half

        l = 0
        r = n

        while l <= r:
            mid = ((r-l)//2) + l
            res = guess(mid)

            if res == 0: return mid
            elif res == -1: r = mid - 1
            else: l = mid + 1

        return 0
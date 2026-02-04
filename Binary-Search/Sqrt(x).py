class Solution:
    def mySqrt(self, x: int) -> int:
        
        # We know a boundary from 1 -> sqrt(x). We are looking
        # for one value in this range, with a clear way of telling
        # which end we need to go (at the midpoint, are we less or
        # greater than our goal?). Simply use binary search

        l = 1
        r = x

        # Wait for the pointers to cross. The last iteration will
        # have l cross r, establishing the upper int bound. This
        # means r will be the correct lower bound. 
        while l <= r:
            mid = int((r-l)/2) + l
            mid2 = mid*mid

            if mid2 == x: return mid

            # Make sure mid is excluded as we tested it already
            elif mid2 > x: r = mid -1
            else: l = mid + 1
        
        return r
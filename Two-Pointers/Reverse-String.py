from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # Use a pointer at the start and end, swapping index values
        # and moving both inward until they meet or cross

        l = 0
        r = len(s) - 1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp 
            l+=1
            r-=1       
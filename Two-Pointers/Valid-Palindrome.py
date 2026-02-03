class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Initialize two pointers, one at start and one at end.
        # Then, simply check values and move both towards center
        # if equal, or return False if not

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l].isalnum():
                if s[r].isalnum():
                    if s[l] == s[r]:
                        l+=1 
                        r-=1
                    else: return False
                else: r -= 1
            else: l += 1
        
        return True
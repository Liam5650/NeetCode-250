class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # Make a hashmap for easy search within string
        s1_dict = {}
        for ch in s1:
            if ch in s1_dict: s1_dict[ch] += 1
            else: s1_dict[ch] = 1
        
        # Build a dict progressively for the main string, checking
        # along the way to see if it matches
        iterated = 0
        s2_dict = {}
        for i in range(len(s2)):

            # Add value if smaller than window size
            if iterated < len(s1):
                ch = s2[i]
                if ch in s2_dict: s2_dict[ch] += 1
                else: s2_dict[ch] = 1
                iterated += 1

            # If we reach the window size, check if equal, otherwise remove
            # the value at the start of the window to slide and continue
            if iterated == len(s1):
                if s1_dict == s2_dict: return True
                else:
                    ch = s2[i-len(s1) + 1]
                    if s2_dict[ch] == 1: s2_dict.pop(ch)
                    else: s2_dict[ch] -= 1
                    iterated -= 1

        return False
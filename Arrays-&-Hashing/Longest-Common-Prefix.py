from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Intuition for this is to just scan across characters
        # one by one in the strings, and returning the result as
        # soon as either diff chars are found, or the length of a 
        # string exceeds another (we are limited by the shortest)

        res = ""

        # Simply take the vals from the first string since we can 
        # get these all easily. No need to pick the shortest string,
        # we check for that later when comparing the index to length
        for i in range(len(strs[0])):

            # The char we are checking if consistent
            candidate = strs[0][i]

            # Check other strings
            for s in strs[1:]:

                # Stop the search early if out of index bounds, or dif char
                if i > len(s)-1 or s[i] != candidate: return res
            res = res + candidate
            i +=1
        
        return res
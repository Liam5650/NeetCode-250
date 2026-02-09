class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # Build the new string one char at a time
        res = ""
        i = 0

        # Go to the end of word 1
        while i < len(word1):
            res += word1[i]

            # Add the char from word2 if it is in range too
            if i < len(word2): res += word2[i]

            i += 1

        # Check to make sure we don't have any chars remaining in word2 as well
        if i < len(word2):
            res += word2[i:]

        return res
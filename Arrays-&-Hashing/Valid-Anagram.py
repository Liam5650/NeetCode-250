class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # This is can be simply done using hashmaps. Iterate
        # through both strings and map to a count for chars, 
        # then see if these two are equal.

        sMap = {}
        for char in s:
            sMap[char] = sMap[char] + 1 if sMap.get(char) != None else 1

        tMap = {}
        for char in t:
            tMap[char] = tMap[char] + 1 if tMap.get(char) != None else 1

        return sMap == tMap
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a dict to store seen char set counts that map to a value of a
        # list that holds the strings found for that set
        char_sets = defaultdict(list)

        # Go through strings and create dicts for them
        for s in strs:
            char_set = {}
            for char in s:
                if char_set.get(char): char_set[char] += 1
                else: char_set[char] = 1

            # Freeze so we make it unmutable and possible to use as the key
            # for the strings associated with it
            char_set = frozenset(char_set.items())

            # Simply append the string to the appropriate set
            char_sets[char_set].append(s)

        return list(char_sets.values())
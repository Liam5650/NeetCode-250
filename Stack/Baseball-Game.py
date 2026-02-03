from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        # Super easy, just use a list as a stack and get the two
        # newest vals (two closest to end) when doing + ops

        scores = []
        for op in operations:
            if op == "+": scores.append(scores[-1] + scores[-2])
            elif op =="D": scores.append(scores[-1] * 2)
            elif op == "C": scores.pop()
            else: scores.append(int(op))

        return sum(scores)
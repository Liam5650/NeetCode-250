from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Simple binary search, with an easy mapping of a 2D coordinate into
        # 1D position.

        # We will segment as if it is a 1D array
        size = len(matrix) * len(matrix[0])
        l = 0
        r = size - 1

        # Binary search
        while l <= r:

            guess = ((r-l) // 2) + l

            # Map the 1D pos back into the 2D pos based on matrix dimensions
            x = guess // len(matrix[0])
            y = guess % len(matrix[0])

            # Standard binary search segmentation
            if matrix[x][y] == target: return True
            elif matrix[x][y] < target: l = guess + 1
            else: r = guess - 1

        return False
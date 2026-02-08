from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        max_depth = 0

        # Simply go through the tree diving deeper and keeping track of depth
        def dive(node, level):
            nonlocal max_depth
            if level > max_depth: max_depth = level
            if node.left: dive(node.left, level + 1)
            if node.right: dive(node.right, level + 1)

        dive(root, 1)
        return max_depth
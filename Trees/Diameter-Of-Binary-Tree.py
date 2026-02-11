from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # The intuition behind this is that at any given node, we want to
        # find the max height of both the left and right paths, which
        # combine to give us the max diameter at that node. We then just
        # continue backwards using the max height + 1 for that processed node

        # Store the max diameter found so far globally
        max_diam = 0 

        # Iterate through nodes recursively
        def dfs(node):

            if not node: return 0

            # Iterate recursively
            left = dfs(node.left)
            right = dfs(node.right)

            # Check if new max is found, and return +1 for the node we just processed
            nonlocal max_diam
            max_diam = max(max_diam, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return max_diam
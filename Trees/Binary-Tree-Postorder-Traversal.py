from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Explore left, then right as far as we can. Then append the val to res
        res = []

        def dfs(node):
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            res.append(node.val)

        if root: dfs(root)
        return res
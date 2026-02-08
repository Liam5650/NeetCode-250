from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Simply iterate recursively as far left as we can go, then append
        # and explore right

        res = []
        def traverse(root):
            if root.left: traverse(root.left)
            res.append(root.val)
            if root.right: traverse(root.right)


        if root: traverse(root)
        return res
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Simply output the node val, then explore left and right
        # recursively (left comes first)
        res = []

        def traverse(node):
            res.append(node.val)
            if node.left: (traverse(node.left))
            if node.right: (traverse(node.right))
        
        if root: traverse(root)
        return res
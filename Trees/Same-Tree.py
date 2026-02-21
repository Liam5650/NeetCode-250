from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def compare(p, q):
            if (p and not q) or (q and not p): return False
            if p == q == None: return
            if p.val != q.val: return False

            compare(p.left, q.left)
            compare(p.right, q.right)

        compare(p, q)
        return True
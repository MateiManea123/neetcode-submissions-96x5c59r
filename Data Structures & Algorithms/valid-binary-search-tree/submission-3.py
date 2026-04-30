# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, interval):
            if root is None:
                return True
            if not(root.val>interval[0] and root.val < interval[1]):
                return False
            
            return bool(dfs(root.left, [interval[0],root.val]) * dfs(root.right, [root.val,interval[1]]))
        return dfs(root,[float("-inf"),float("inf")])
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if not root:
            return []
        q.append([root,1])
        while q:
            print(q)
            node,lvl = q.popleft()
            if node.left:
                q.append([node.left,lvl+1])
            if node.right:
                q.append([node.right,lvl+1])
            if len(q) == 0 or lvl!=q[0][1]:
                res.append(node.val)


       

        return res
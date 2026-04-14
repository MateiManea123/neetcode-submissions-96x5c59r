# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = collections.deque()
        q.append((root, 1))

        while q:
            semires = []

            node, lvl = q.popleft()
            semires.append(node.val)

            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))

            while q and q[0][1] == lvl:
                node2, _ = q.popleft()
                semires.append(node2.val)

                if node2.left:
                    q.append((node2.left, lvl + 1))
                if node2.right:
                    q.append((node2.right, lvl + 1))

            res.append(semires)

        return res
        
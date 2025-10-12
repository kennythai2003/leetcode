# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        if not root.left and not root.right: 
            return [root.val]
        left = []
        right = []
        bottom = []
        def dfs(cur, onLeft,onRight):
            if not cur:
                return
            if not cur.left and not cur.right:
                bottom.append(cur.val)
                return
            if onLeft:
                left.append(cur.val)
            if onRight:
                right.append(cur.val)
            dfs(cur.left,onLeft, onRight and not cur.right)
            dfs(cur.right, onLeft and not cur.left, onRight)
        dfs(root.left, True, False)
        dfs(root.right,False, True)
        return [root.val] + left + bottom + right[::-1]
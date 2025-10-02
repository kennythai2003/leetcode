# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = 0
        def dfs(curr):

            if not curr:
                return [True, 0]
            
            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left[1] + right[1])
            
            balance = left[0] and right[0] and abs(left[1] - right[1]) < 2
            
            return [balance, 1 + max(left[1], right[1])]

        return dfs(root)[0]
        
        return dfs(root)[1]


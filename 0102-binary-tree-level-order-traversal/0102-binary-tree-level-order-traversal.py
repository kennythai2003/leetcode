# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()

        queue.append(root)

        while queue:
            levels = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    levels.append(curr.val)
                    queue.append(curr.left)
                    queue.append(curr.right)
            if levels:
                res.append(levels)


        return res
        
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

        queue = deque()
        queue.append(root)

        while queue:
            levels = []
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    levels.append(curr.val)

            if levels:
                res.append(levels)
        
        return res
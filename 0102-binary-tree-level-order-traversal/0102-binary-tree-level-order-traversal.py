# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        queue = deque()
        res = []

        if not root: 
            return res
        curr = root
        queue.append(curr)

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if level:
                res.append(level)
        
        return res

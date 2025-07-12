class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for i in range(1, n):
            for j in range(n):
                left = matrix[i - 1][j - 1] if j > 0 else float('inf')
                up = matrix[i - 1][j]
                right = matrix[i - 1][j + 1] if j < n - 1 else float('inf')
                matrix[i][j] += min(left, up, right)

        return min(matrix[-1])

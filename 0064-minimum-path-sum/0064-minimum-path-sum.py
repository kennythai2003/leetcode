class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # Initialize first column
        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        # Initialize first row
        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]

        # Fill in the rest of the grid
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[n - 1][m - 1]

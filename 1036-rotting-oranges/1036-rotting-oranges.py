class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        fresh = 0
        mins = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        if not grid:
            return -1

        queue = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))

        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    newrow, newcol = row + dr, col + dc
                    if (newrow < 0 or newcol < 0 or newrow >= ROWS or newcol >= COLS or grid[newrow][newcol] == 2 or grid[newrow][newcol] == 0):
                        continue
                    
                    grid[newrow][newcol] = 2
                    queue.append((newrow, newcol))
                    fresh -= 1
            mins +=  1

        return mins if not fresh else -1

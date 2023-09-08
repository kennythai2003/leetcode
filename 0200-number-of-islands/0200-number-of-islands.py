class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid: 
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
                
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    self.bfs(grid, r, c, visit)
                    islands += 1
        return islands
    
    def bfs(self, grid, r, c, visit):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        queue.append((r, c))
        visit.add((r, c))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                r,c = row + dr, col + dc
                
                if (r < 0 or c < 0 or
                    r == ROWS or c == COLS or
                    (r, c) in visit or grid[r][c] == "0"):
                    continue
                    
                queue.append((r, c))
                visit.add((r, c))

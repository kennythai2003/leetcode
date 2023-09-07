class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        fresh = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    if (r + dr < 0 or c + dc < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        grid[r + dr][c + dc] == 0 or grid[r + dr][c + dc] == 2):
                        continue
                    grid[r + dr][c + dc] = 2
                    queue.append((r + dr, c + dc))
                    fresh -= 1
            minutes += 1

        if fresh == 0:
            return minutes
        else:
            return -1
                    
            

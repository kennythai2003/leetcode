class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return -1

        fresh = 0
        mins = 0
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh:
            for i in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (min(r, c) < 0 or r == len(grid) or c == len(grid[0]) 
                        or grid[r][c] == 0 or grid[r][c] == 2):
                        continue
                    
                    queue.append((r, c))
                    grid[r][c] = 2
                    fresh -= 1
            mins += 1
        
        return -1 if fresh else mins
            

                
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return -1
        
        fresh = 0
        queue = deque()
        time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))

        while queue and fresh:
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions: 
                    row, col= dr + r, dc + c
                    if (min(row, col) < 0 or row == len(grid) or col == len(grid[0]) 
                        or grid[row][col] == 0 or grid[row][col] == 2):
                        continue
                    
                    queue.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1
            time += 1
        
        return time if not fresh else -1
        
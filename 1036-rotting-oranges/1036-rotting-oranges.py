class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque() 
        # visit = set()

        fresh = 0
        time = 0

        if not grid:
            return -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
        
        while queue and fresh > 0:

            for i in range(len(queue)):

                row, col = queue.popleft()
                for dr, dc in directions:
                    drow = row + dr
                    dcol = col + dc
                    if (min(drow, dcol) < 0 or drow == len(grid) or dcol == len(grid[0]) or
                    grid[drow][dcol] == 0 or  grid[drow][dcol] == 2):
                        continue

                    grid[drow][dcol] = 2
                    queue.append((drow, dcol))
                    fresh -= 1
                    # visit.add((drow,dcol))
                
            time += 1
            
        return time if not fresh else -1

                

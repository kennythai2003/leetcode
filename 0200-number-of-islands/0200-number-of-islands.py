class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        directions = [[1,0], [-1,0], [0,1],[0, -1]]
        if not grid: return 0
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            
            while queue:
                # for each element in the queue, pop it and explore its neighbors
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    
                    # explore neighbors
                    for dr, dc in directions:
                        newr, newc = row + dr, col + dc

                        if (newr < 0 or newc < 0 or newr == ROWS or newc == COLS or
                            grid[newr][newc] == "0" or (newr, newc) in visit):
                            continue
                        
                        queue.append((newr, newc))
                        visit.add((newr, newc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    bfs(r, c)
        
        return islands
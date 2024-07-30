class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxa = 0
        directions = [[1,0], [-1,0], [0,1],[0, -1]]
        if not grid: return 0
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            area = 1
            while queue:
                # for each element in the queue, pop it and explore its neighbors
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    
                    # explore neighbors
                    for dr, dc in directions:
                        newr, newc = row + dr, col + dc

                        if (newr < 0 or newc < 0 or newr == ROWS or newc == COLS or
                            grid[newr][newc] == 0 or (newr, newc) in visit):
                            continue
                        area += 1
                        queue.append((newr, newc))
                        visit.add((newr, newc))

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxa = max(maxa, bfs(r, c))
        
        return maxa
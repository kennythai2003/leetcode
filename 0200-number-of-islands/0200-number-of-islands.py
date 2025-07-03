class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        visit = set()
        islands = 0

        def bfs (r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        drow, dcol = row + dr, col + dc
                        if (min(drow, dcol) < 0 or drow == len(grid) or dcol == len(grid[0]) or (drow, dcol) in visit or grid[drow][dcol] == "0"):
                            continue
                        
                        queue.append((drow, dcol))
                        visit.add((drow, dcol))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visit = set()
        islands = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(rd, cd):
            queue = deque()
            queue.append((rd, cd))
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in directions:
                        row, col = r + dr, c + dc
                        if (min(row, col) < 0 or row == len(grid) or col == len(grid[0]) or
                            (row, col) in visit or grid[row][col] == "0"):
                            continue
                        queue.append((row, col))
                        visit.add((row, col))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visit and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        
        return islands
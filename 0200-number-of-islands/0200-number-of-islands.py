class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        DIRECTIONS = [(1, 0), (-1 , 0), (0, 1), (0, -1)]

        visit = set()
        islands = 0
        if not grid: return 0 

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()

                    for dr, dc in DIRECTIONS:
                        row = dr + r
                        col = dc + c

                        if row == ROWS or col == COLS or row < 0 or col < 0 or (row, col) in visit or grid[row][col] == "0":
                            continue
                        
                        queue.append((row, col))
                        visit.add((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands
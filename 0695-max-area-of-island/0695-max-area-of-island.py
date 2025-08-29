class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        res = 0
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            area = 1
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()

                    for dr, dc in directions:
                        drow, dcol = dr + row, dc + col
                        if (min(drow, dcol) < 0 or drow == len(grid) 
                            or dcol == len(grid[0]) or (drow, dcol) in visit or
                            grid[drow][dcol] == 0):
                            continue
                        
                        queue.append((drow, dcol))
                        visit.add((drow, dcol))
                        area += 1
            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1 and (i, j) not in visit:
                    res = max(bfs(i, j), res)
        
        return res

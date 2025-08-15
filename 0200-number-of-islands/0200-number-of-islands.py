class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        visit = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            visit.add((i, j))

            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        row, col = dr + r, dc + c
                        if (min(row, col) < 0 or row == len(grid) or col == len(grid[0]) 
                            or grid[row][col] == "0" or (row, col) in visit):
                            continue
                        
                        queue.append((row, col))
                        visit.add((row, col))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    res += 1
        
        return res

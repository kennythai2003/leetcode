class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, -1), (1, 1), (-1, 1)]
        short = 1

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        visit = set()

        if not grid: return -1

        if grid[0][0] == 1:
            return -1 

        q.append((0, 0))
        visit.add((0, 0))

        while q:
            
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return short
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if (row == ROWS or col == COLS or row < 0 or col < 0
                        or grid[row][col] == 1 or (row, col) in visit): 
                        continue
                    
                    q.append((row, col))
                    visit.add((row, col))

            short += 1
        return -1 
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                    (1, -1), (1, 1), (-1, 1), (-1, -1)]
        shortest = 1
        queue = deque()
        queue.append((0, 0))
        visit = set()
        visit.add((0, 0))
        if not grid: return -1
        if grid[0][0] == 1: return -1 

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return shortest

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or
                        (row, col) in visit or grid[row][col] == 1):
                        continue

                    visit.add((row, col)) 
                    queue.append((row, col))
            shortest += 1
        return -1 
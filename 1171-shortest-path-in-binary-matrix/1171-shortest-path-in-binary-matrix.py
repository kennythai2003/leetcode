class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, - 1), (-1, 1), (-1, -1)]

        if grid[0][0] == 1 or not grid:
            return -1 
        
        queue = deque()
        visit = set()
        queue.append((0, 0))
        visit.add((0, 0))
        path = 1

        while queue:
            for i in range(len(queue)):

                r, c = queue.popleft()
                if (r == len(grid) - 1) and (c == len(grid[0]) - 1):
                    return path
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c

                    if (min(row, col) < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 1 or (row, col) in visit):
                        continue
                    
                    queue.append((row, col))
                    visit.add((row, col))
                
            path += 1
        
        return -1
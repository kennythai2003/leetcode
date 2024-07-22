class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, - 1], [1, 1], [-1, 1], [-1, -1]]

        queue = deque()
        queue.append((0, 0))
        visit = set()
        visit.add((0, 0))
        length = 1 

        if grid[0][0] == 1:
            return -1

        while queue:
            
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    newrow = dr + r 
                    newcol = dc + c
                    if (newrow < 0 or newcol < 0 or
                        newrow == ROWS or newcol == COLS or
                        (newrow, newcol) in visit or
                        grid[newrow][newcol] == 1):
                        continue
                    
                    queue.append((newrow, newcol))
                    visit.add((newrow, newcol))
            length += 1
        
        return -1
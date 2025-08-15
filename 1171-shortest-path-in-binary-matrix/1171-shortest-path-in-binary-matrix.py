class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, 1), (-1, -1)]

        if not grid or grid[0][0] == 1:
            return -1
        
        length = 1
        queue = deque()
        queue.append((0, 0))
        
        visit = set()
        visit.add((0, 0))

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == len(grid) - 1 and c == len(grid[0]) - 1:
                    return length
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (min(row, col) < 0 or row == len(grid) or col == len(grid[0]) or
                        grid[row][col] == 1 or ((row, col) in visit)):
                        continue
                
                    queue.append((row, col))
                    visit.add((row, col))
                    
            length += 1
        
        return -1


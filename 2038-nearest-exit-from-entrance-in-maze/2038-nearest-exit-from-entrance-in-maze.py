class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS = len(maze)
        COLS = len(maze[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        res = 0
        

        if not maze:
            return 0

        queue = deque()
        visit = set()
        queue.append((entrance[0], entrance[1], 0))
        visit.add((entrance[0], entrance[1]))

        while queue:
            for i in range(len(queue)):
                r, c, d = queue.popleft()

                for dr, dc in DIRECTIONS:
                    row = dr + r
                    col = dc + c
                    
                    if (row == ROWS or col == COLS or row < 0 or col < 0 or (row, col) in visit or maze[row][col] == "+"):
                        continue
                    
                    if (row == 0 or col == 0 or row == ROWS - 1 or col == COLS - 1):
                        return d + 1

                    queue.append((row, col, d + 1))
                    visit.add((row, col))
        return -1
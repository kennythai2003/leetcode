class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashm = {}
        rep = 0
        miss = 0
        for i in range(len(grid[0])):
            for j in range(len(grid[0])):
                if (grid[i][j] not in hashm):
                    hashm[grid[i][j]] = 0
                hashm[grid[i][j]] += 1
        
        for num in range(1, (len(grid) * len(grid) + 1)):
            if num not in hashm:
                miss = num
            elif hashm[num] == 2:
                rep = num
        
        return [rep, miss]
                 
            

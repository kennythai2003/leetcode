class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix) - 1

        while l < r:

            t, b = l, r

            for i in range(r - l):
                
                temp = matrix[t][l + i]

                # tl <- bl
                matrix[t][l + i] = matrix[b - i][l]

                # bl <- br
                matrix[b - i][l] = matrix[b][r -i]

                # br <- tr
                matrix[b][r-i] = matrix[t + i][r]

                # tr <- temp
                matrix[t + i][r] = temp
            
            l, r = l + 1, r - 1
            
        return matrix
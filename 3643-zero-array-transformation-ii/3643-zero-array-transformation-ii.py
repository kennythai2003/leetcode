class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        dif_arr = [0] * (n + 1) 
        cur_sum = j = 0 

        for i, num in enumerate(nums):
            cur_sum += dif_arr[i]

            while j < m and cur_sum < num: 
                l, r, val = queries[j]
                j += 1

                if i < l:
                    dif_arr[l] += val 
                elif i <= r:
                    cur_sum += val 
                    
                dif_arr[r + 1] -= val 

            if cur_sum < num:
                return -1 
            
        return j 
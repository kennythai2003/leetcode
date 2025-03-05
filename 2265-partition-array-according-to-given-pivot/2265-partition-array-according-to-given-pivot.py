class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i1, j1 = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1
        res = [0] * len(nums)

        while i1 < len(nums):

            if nums[i1] < pivot:
                res[i2] = nums[i1]
                i2 += 1
            
            if nums[j1] > pivot:
                res[j2] = nums[j1]
                j2 -= 1
            
            i1, j1 = i1 + 1, j1 - 1
        
        while i2 <= j2:
            res[i2] = res[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1

        return res 
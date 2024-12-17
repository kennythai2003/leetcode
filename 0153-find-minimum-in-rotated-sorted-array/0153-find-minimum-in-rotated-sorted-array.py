class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mini = nums[l]
        while l <= r:

            if nums[l] <= nums[r]:
                return min(nums[l], mini)

            m = (l + r) // 2
            mini = min(mini, nums[m])
            if nums[m] <= nums[r]:
                r = m - 1
            else:
                l = m + 1
            
        
        return mini


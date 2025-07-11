class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[l]
        while l <= r:

            if nums[l] < nums[r]:
                minimum = min(nums[l], minimum)
            
            m = (l + r) // 2
            minimum = min(nums[m], minimum)

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return minimum

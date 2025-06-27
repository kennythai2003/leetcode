class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        minn = nums[l]

        while l <= r:

            if nums[l] < nums[r]:
                minn = min(minn, nums[l])

            m = (l + r) // 2
            minn = min(nums[m], minn)

            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return minn
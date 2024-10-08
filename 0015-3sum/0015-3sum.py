class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, v in enumerate(nums):
            
            if i > 0 and nums[i - 1] == v:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                
                if nums[l] + nums[r] + v < 0:
                    l += 1
                elif nums[l] + nums[r] + v > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], v])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res
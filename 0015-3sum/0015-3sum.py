class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i, t in enumerate(nums):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:

                if t + nums[l] + nums[r] < 0:
                    l += 1
                elif t + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], t])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevdiffs = {}

        for i, n in enumerate(nums):

            if target - n in prevdiffs:
                return [prevdiffs[target - n], i]
            
            prevdiffs[n] = i
        
        return []
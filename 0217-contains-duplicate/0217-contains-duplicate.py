class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevdiffs = {}
        
        for num in nums:
            if num in prevdiffs:
                return True
            prevdiffs[num] = 1

        return False
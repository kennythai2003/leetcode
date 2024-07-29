class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        diffs = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in diffs:
                return [diffs[diff], i]
            diffs[v] = i
        
        return []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_map:
                return [i, num_map[diff]]
            num_map[n] = i
        
        return []
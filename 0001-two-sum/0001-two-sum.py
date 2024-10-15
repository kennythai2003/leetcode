class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffmap = {}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in diffmap:
                return [i, diffmap[diff]]
            diffmap[v] = i
        
        return []
        
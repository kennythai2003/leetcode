class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsmap = {}

        for n in nums:
            if n in numsmap:
                return True
            numsmap[n] = 1
        
        return False
        
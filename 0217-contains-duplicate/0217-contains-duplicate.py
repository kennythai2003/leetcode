class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nummap = {}

        for n in nums:

            if n in nummap:
                return True
            nummap[n] = 1
        
        return False
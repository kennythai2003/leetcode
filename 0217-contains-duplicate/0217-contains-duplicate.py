class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}

        for num in nums:

            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True
        
        return False
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            length = 0
            if n - 1 not in nums:
                while n + length in nums:
                    length += 1
            res = max(res, length)
        
        return res
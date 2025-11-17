class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in numset:
            length = 1
            if n - 1 not in numset:
                while n + length in numset:
                    length += 1
            
            res = max(length, res)

        return res
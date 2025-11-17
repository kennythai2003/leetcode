class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        for n in numset:
            length = 1
            if n - 1 not in numset:
                while n + length in numset:
                    res = max(res, length)
                    length += 1

        return res
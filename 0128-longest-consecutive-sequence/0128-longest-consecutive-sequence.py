class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in numset:
            length = 0
            if n - 1 not in numset: 
                while n + length in numset:
                    length += 1
            longest = max(longest, length)

        return longest
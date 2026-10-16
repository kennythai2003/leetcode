class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in diff_map:
                return [diff_map[diff], i]
            
            diff_map[n] = i
        
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_map = {}
        for n in nums:
            num_map[n] = 1 + num_map.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for key, v in num_map.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
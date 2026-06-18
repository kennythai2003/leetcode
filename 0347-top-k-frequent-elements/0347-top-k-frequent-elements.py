class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        res = []
        for n in nums:
            nums_map[n] = 1 + nums_map.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for i, v in nums_map.items():
            freq[v].append(i)
        
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
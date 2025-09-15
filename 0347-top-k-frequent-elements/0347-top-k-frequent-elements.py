class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nummap = {}
        res = []
        for n in nums:
            nummap[n] = 1 + nummap.get(n, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for i, v in nummap.items():
            freq[v].append(i)
        
        for i in range(len(freq) - 1, -1, -1):

            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
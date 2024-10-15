class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsmap = {}
        for num in nums:
            numsmap[num] = 1 + numsmap.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for i, v in numsmap.items():
            freq[v].append(i)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


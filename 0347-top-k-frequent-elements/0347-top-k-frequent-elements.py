class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for num in nums:
            numsmap[num] = 1 + numsmap.get(num, 0)
        
        for i, v in numsmap.items():
            freq[v].append(i)
        
        for i in range(len(freq) - 1, -1 ,-1):

            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
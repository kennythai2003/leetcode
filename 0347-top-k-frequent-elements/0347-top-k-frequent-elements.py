class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a nummap
        nummap = {}
        for n in nums:
            nummap[n] = 1 + nummap.get(n, 0)

        numfreq = [[] for i in range(len(nums) + 1)] 
        for i, v in enumerate(nummap):
            numfreq[v].append(i)

        res = []
        for i in range(len(numfreq) - 1, -1, -1):
            for j in numfreq[i]:
                if len(res) == k:
                    return res
        
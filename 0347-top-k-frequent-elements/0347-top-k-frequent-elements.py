class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        res = []

        for num in nums:
            countmap[num] = 1 + countmap.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for i, v in countmap.items():
            freq[v].append(i)
        
        for i in range(len(freq) - 1, -1, -1):

            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        






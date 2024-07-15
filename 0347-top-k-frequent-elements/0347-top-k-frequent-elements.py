class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsmap = {}
        freq = [[] for i in range(len(nums) + 1)]
        result = []

        for n in nums:
            numsmap[n] = 1 + numsmap.get(n, 0)
        

        for i, v in numsmap.items():
            freq[v].append(i)
        
        for i in range(len(freq) - 1, -1, -1):

            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
        
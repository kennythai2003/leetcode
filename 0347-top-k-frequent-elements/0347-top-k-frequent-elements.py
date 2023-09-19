class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #  hashmap to count elements
        # inverse array
        # loop through array

        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        arr = [[] for i in range(len(nums) + 1)]

        for i, v in hashmap.items():
            arr[v].append(i)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for j in arr[i]:
                res.append(j)
                if len(res) == k:
                    return res

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mh = nums
        self.k = k
        heapq.heapify(self.mh)
        while len(self.mh) > k:
            heapq.heappop(self.mh)


    def add(self, val: int) -> int:
        heapq.heappush(self.mh, val)
        while len(self.mh) > self.k:
            heapq.heappop(self.mh)
        return self.mh[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
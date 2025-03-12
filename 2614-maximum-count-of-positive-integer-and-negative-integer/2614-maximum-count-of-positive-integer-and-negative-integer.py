class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negcntr = 0
        poscntr = 0

        for num in nums:
            if num < 0: 
                negcntr += 1
            
            if num > 0:
                poscntr += 1
        
        return max(negcntr, poscntr)
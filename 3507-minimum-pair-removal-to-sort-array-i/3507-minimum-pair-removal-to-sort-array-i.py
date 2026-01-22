class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        # 1. nums is already a list (dynamic array in Python)
        operations = 0
        
        # Helper function to check non-decreasing status
        def is_non_decreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        # 2. While loop to check status
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            target_index = -1
            
            # 3. Find leftmost pair with minimum sum
            for i in range(len(nums) - 1):
                current_sum = nums[i] + nums[i + 1]
                if current_sum < min_sum:
                    min_sum = current_sum
                    target_index = i
            
            # 4. Replace pair with their sum
            if target_index != -1:
                nums[target_index] = min_sum
                nums.pop(target_index + 1)
                operations += 1
                
        return operations
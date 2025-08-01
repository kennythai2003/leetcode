class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxa = 0


        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxa = max(maxa, area)

            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return maxa

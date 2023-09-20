class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l, r = 0, len(height) - 1
        maxa = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxa = max(area, maxa)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxa
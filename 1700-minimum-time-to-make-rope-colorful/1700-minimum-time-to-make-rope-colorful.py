class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        time = 0
        max_cost = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                max_cost = 0
            
            time += min(max_cost, neededTime[i])
            max_cost = max(max_cost, neededTime[i])
        
        return time
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                ____, indx = stack.pop()
                answer[indx] = i - indx
            
            stack.append([t, i])
        
        return answer
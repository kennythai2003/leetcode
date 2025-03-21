class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
        
            while stack and t > stack[-1][0]:
                ___, ind = stack.pop()
                answer[ind] = i - ind
            
            stack.append([t, i])

        return answer
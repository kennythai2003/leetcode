class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # To store the final result
        self.backtrack(candidates, 0, target, [], res)
        return res

    def backtrack(self, candidates, start, target, comb, res):
        if target == 0:
            res.append(list(comb))
            return

        for i in range(start, len(candidates)):
            if target < candidates[i]:
                continue
            comb.append(candidates[i])
            self.backtrack(candidates, i, target - candidates[i], comb, res)
            comb.pop()
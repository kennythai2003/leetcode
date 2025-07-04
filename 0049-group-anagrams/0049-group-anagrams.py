class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            cmap = [0] * 26
            for c in s:
                cmap[ord(c) - ord('a')] += 1

            res[tuple(cmap)].append(s)

        return list(res.values())
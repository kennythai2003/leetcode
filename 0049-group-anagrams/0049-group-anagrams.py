class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:
            alpas = [0] * 26
            for c in s:
                alpas[ord(c) - ord('a')] += 1
            
            res[tuple(alpas)].append(s)
        
        return res.values()

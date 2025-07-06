class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = defaultdict(list)

        for s in strs:
            charcnt = [0] * 26
            for c in s:
                charcnt[ord(c) - ord('a')] += 1
            smap[tuple(charcnt)].append(s)
        
        return list(smap.values())
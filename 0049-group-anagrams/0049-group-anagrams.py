class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for s in strs:
            lett_map = [0] * 26
            for c in s:
                lett_map[ord(c) - ord('a')] += 1
            
            anagrams_map[tuple(lett_map)].append(s)
        
        return list(anagrams_map.values())
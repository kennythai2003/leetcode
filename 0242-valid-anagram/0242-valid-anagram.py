class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}

        if len(s) != len(t):
            return False

        for c in s:
            smap[c] = 1 + smap.get(c, 0) 
        
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        
        for i in smap:
            if smap[i] != tmap.get(i, 0):
                return False

        return True

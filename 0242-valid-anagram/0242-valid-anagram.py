class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap, tmap = {}, {}

        if len(s) != len(t):
            return False

        for i in s:
            smap[i] = 1 + smap.get(i, 0)
        
        for i in t:
            tmap[i] =1 + tmap.get(i, 0)
        

        for j in smap:
            if smap[j] != tmap.get(j , 0):
                return False

        return True
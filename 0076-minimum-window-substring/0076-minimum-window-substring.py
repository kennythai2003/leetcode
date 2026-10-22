class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""

        s_map, t_map = {}, {}
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        have, need = 0, len(t_map)
        res, res_len = [-1, -1], float("infinity")

        l = 0

        for r in range(len(s)):
            c = s[r]
            s_map[c] = 1 + s_map.get(c, 0)

            if c in t_map and s_map[c] == t_map[c]:
                have += 1

            while have == need:
                
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                s_map[s[l]] -= 1
                if s[l] in t_map and s_map[s[l]] < t_map[s[l]] :
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_map = {}
        for c in text:
            char_map[c] = 1 + char_map.get(c, 0)
        
        return min(
            char_map.get("b", 0),
            char_map.get("a", 0),
            char_map.get("l", 0) // 2,
            char_map.get("o", 0) // 2,
            char_map.get("n", 0)
        )
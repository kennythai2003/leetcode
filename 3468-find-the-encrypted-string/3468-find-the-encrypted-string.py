class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
        res = ""
        length = len(s)

        for i in range(length):
            res += s[(i + k) % length]
        
        return res
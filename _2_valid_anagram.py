class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26
        for a in s:
            idx = ord(a) - ord('a')
            alpha[idx] += 1
        for a in t:
            idx = ord(a) - ord('a')
            alpha[idx] -= 1
        for n in alpha:
            if n != 0:
                return False
        return True
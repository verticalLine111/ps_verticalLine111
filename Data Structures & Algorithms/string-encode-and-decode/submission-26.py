class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            res += str(len(strs[i])) + "#" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l:r])
            rs = s[r + 1 : r + length + 1]
            res.append(rs)
            l = r + length + 1
        return res

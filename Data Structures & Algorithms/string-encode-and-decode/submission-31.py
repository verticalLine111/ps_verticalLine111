class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs)):
            res += str(len(strs[i])) + '#' + strs[i]
        return res
    def decode(self, s: str) -> List[str]:
        r = 0
        res =[]
        while r < len(s):
            l = r
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            res.append(s[r+1 : r + 1 + length])
            r = r + length +1 
        
        return res

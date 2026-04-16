class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fmap = defaultdict(list)
        for i in range(len(strs)):
            alph = [0] * 26
            for j in range(len(strs[i])):
                alph[ord(strs[i][j])-ord('a')] += 1    
            fmap[tuple(alph)].append(strs[i])
        res = []
        for k, v in fmap.items():
            res.append(v)
        return res
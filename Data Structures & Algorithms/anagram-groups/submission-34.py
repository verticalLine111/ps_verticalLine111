class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fmap = defaultdict(list)
        for i in range(len(strs)):
            alph = [0] * 26
            for c in strs[i]:
                idx = ord(c) - ord('a')
                alph[idx] += 1
            fmap[tuple(alph)].append(strs[i])
        res = []
        for k,v in fmap.items():
            res.append(v)
        return res

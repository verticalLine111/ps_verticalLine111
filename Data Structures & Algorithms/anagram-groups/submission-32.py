class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        fmap = defaultdict(list)
        for i in range(len(strs)):
            alph = [0] * 26
            for c in strs[i]:
                alph[ord(c) - ord('a')] += 1
            fmap[tuple(alph)].append(strs[i])
        
        for key, val in fmap.items():
            res.append(val)
        
        return res
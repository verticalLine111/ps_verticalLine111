class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countarr = []
        for i in range(len(nums)):
            countarr.append([])
        countarr.append([])

        nmap = Counter(nums)
        for key,val in nmap.items():
            countarr[val].append(key)
        
        res = []
        print(countarr)
        for i in range(len(countarr)-1, -1, -1):
            if len(countarr[i]) > 0 and len(res) < k:
                for c in countarr[i]:
                    res.append(c)
        return res
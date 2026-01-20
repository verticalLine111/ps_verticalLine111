def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        sortedStrs = []
        for i in range(len(strs)):
            sortedStrs.append("".join(sorted(strs[i]))) 

        strMap = {} 
        for i in range(len(strs)):
            tempKey = "".join(sorted(strs[i]))
            if tempKey in strMap:
                strMap[tempKey].append(strs[i])
            else:
                strMap[tempKey] = [strs[i]]
                

        strKeys = strMap.keys()
        for key in strKeys:
            answer.append(strMap[key])

        return answer

def encode(strs: list[str]) -> str:
    encodeStr= ''
    for i in range(len(strs)):
        encodeStr += str(len(strs[i])) + '#' + strs[i]
    return encodeStr
    
def decode(s: str) -> list[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j+= 1
        length = int(str(s[i:j]))
        i = j+1
        j = i + length
        res.append(s[i:j])
        i = j
    return res

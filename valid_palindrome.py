def valid_palindrome(s: str) -> bool:
    record = []
    strToCheck = s.replace("!", "").replace("?", "").upper()
    for char in strToCheck:
        record.append(char)
    
    count = 0
    while len(record) > 0: 
        if strToCheck[count] == record.pop(): 
            count+=1 
            continue
        else:
            return False
    return True
res = valid_palindrome(s="Was it a car or a cat I saw?")
print(res)
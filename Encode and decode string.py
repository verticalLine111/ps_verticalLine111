def encode( strs: list[str]) -> str:
    if len(strs) == 0:
        return ';'

    for i in strs:

    
    return ";".join(strs)

def decode( s: str) -> list[str]:
    return s.split(';')

dummy_input=[]
print(encode(strs=dummy_input))
print(decode(encode(strs=dummy_input)))

# 타입이 바뀌는게 문제
# 분리된 여러 스트링 리스트를 하나의 스트링으로 잠깐 합쳤다가
# 다시 그걸 분리해서 출력하는 것

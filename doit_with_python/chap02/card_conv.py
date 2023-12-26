# 10진수 정수 x -> 2~36진수 r로 변환
def card_conv(x: int, r: int) -> str:
    
    d = ''
    dchar = '0123456789ABCDEFGHIGKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]

# d = card_conv(4768, 16)
# print(d)

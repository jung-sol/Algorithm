# 알고리즘 개선 1
# 1000 이하의 소수 구하기 #2
# prime1.py 에서 개선 -> 홀수만을 대상으로, 이미 찾은 소수가 계속 그 대상이 된다는 것에서 착안

cnt = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2              # 소수 2를 초기값으로 지정
ptr += 1

for n in range(3, 1001, 2): # 홀수만을 대상으로
    for i in range(1, ptr): # 이미 찾은 소수로 나눔
        cnt += 1
        if n % prime[i] == 0:
            break
    else:                   # 끝까지 나누어 떨어지지 않으면
        prime[ptr] = n      # 소수 배열에 등록
        ptr += 1

for i in range(ptr):
    print(prime[i])

print(f'나눗셈 실행 횟수: {cnt}')   # 14622


# 1000 이하의 소수 모두 구하기 # 1

data = []
cnt = 0

for i in range(2, 1000):
    for j in range(2, i):
        cnt += 1
        if i % j == 0:
            break
    else:   # 끝까지 나누어 떨어지지 않으면 수행
        data.append(i)

print(data)
print(f'나눗셈 실행 횟수: {cnt}')   # 78022

import time
# M 더하는 횟수
# K 연속 더하는 횟수
# N 배열의 크기

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
sec = data[n - 2]

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * sec

print(result)

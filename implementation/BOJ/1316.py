n = int(input())

for _ in range(n):
    s = input()

    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            pass
        elif s[i] in s[:i - 1]:
            n -= 1
            break
print(n)

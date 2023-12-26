from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]

if __name__ == '__main__':
    print('배열을 역순으로 정렬')
    num = int(input('원소 개수 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]값 입력: '))

    reverse_array(x)

    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 이진 검색 알고리즘

from typing import Sequence, Any

def bin_search(a: Sequence, key: Any) -> int:

    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2

        if a[pc] < key:
            pl = pc + 1

        elif a[pc] == key:
            return pc

        else a[pc] > key:
            pr = pc - 1

        if pl > pr:
            break
        
    return -1

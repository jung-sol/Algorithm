# 퀵정렬 구현
arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
            
        while right > start and array[right] >= array[pivot]:
            right -= 1
            
        if left > right:    # 엇갈린 경우 -> 작은 값과 피벗 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array, start, right - 1) # 분할 후 왼쪽
    quick_sort(array, right + 1, end) # 분할 후 오른쪽
    

quick_sort(arr, 0, len(arr) - 1)

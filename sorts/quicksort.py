def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def partition(arr, l, r):
    pivot = arr[(l + r)//2]
    i = l
    j = r
    while i <= j:
        while (arr[i] < pivot):
            i += 1
        while (arr[j] > pivot):
            j -= 1
        if i <= j:
            swap(arr, i, j)
            i += 1
            j -= 1
        return i

def qs(arr, l, r):
    if (len(arr) > 1):
        index = partition(arr, l, r)
        if l < index-1:
            qs(arr, l, index-1)
        if r > index:
            qs(arr, index, r)
    return arr

def quicksort(arr):
    return qs(arr, 0, len(arr)-1)

qsarr = quicksort([1,9,4,6,2,35,1,231,6,6,2])
print(qsarr)

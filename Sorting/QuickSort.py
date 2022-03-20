def findPivot(list, start, end):
    assumedPivot = list[end]
    i = start-1
    for j in range(start, end):
        if(assumedPivot > list[j]):
            i += 1
        list[i], list[j] = list[j], list[i]
    list[i+1], list[end] = list[end], list[i+1]
    return i+1


def quickSort(list, start, end):
    if(start < end):
        pivot = findPivot(list, start, end)
        quickSort(list, start, pivot-1)
        quickSort(list, pivot+1, end)


L = list(map(int, input().strip().split()))
quickSort(L, 0, len(L)-1)
print(L)

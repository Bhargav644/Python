def insertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        current = list[i]
        while(j >= 0 and list[j] > current):
            list[j+1] = list[j]
            j -= 1
            list[j+1] = current
    return list


list = [9, 5, 4, 6, 2, 1, 0]
print(insertionSort(list))

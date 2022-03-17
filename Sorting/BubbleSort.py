def bubbleSort(list):
    for i in range(1, len(list)):
        for j in range(0, len(list)-1):
            if(list[j] > list[i]):
                (list[j], list[i]) = (list[i], list[j])
    return list


list = [6, 5, 4, 3, 2, 1]
print(bubbleSort(list))

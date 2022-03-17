def merge(list1, list2):
    (i, j, k) = (0, 0, 0)
    final = []
    while(k < len(list1)+len(list2)):
        if(i == len(list1)):
            final.extend(list2[j:])
            k += (len(list2)-j)
        elif(j == len(list2)):
            final.extend(list1[i:])
            k += (len(list1)-i)
        elif(list1[i] < list2[j]):
            final.append(list1[i])
            i += 1
            k += 1
        else:
            final.append(list2[j])
            j += 1
            k += 1
    return final


def mergeSort(list):
    n = len(list)
    if(n <= 1):
        return list
    list1 = mergeSort(list[:n//2])
    list2 = mergeSort(list[n//2:])
    final = merge(list1, list2)
    return final


list = list(map(int, input().strip().split()))
print(mergeSort(list))

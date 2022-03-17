def binarySearch(list, key):
    if(list != []):
        mid = (len(list))//2
        if(list[mid] == key):
            return True
        elif(list[mid] > key):
            return binarySearch(list[0:mid], key)
        else:
            return binarySearch(list[mid+1:len(list)], key)
    else:
        return False


key = int(input())
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if(binarySearch(list, key)):
    print("Found")
else:
    print("Not Found")

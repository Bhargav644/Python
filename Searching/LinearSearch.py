def linearSearch(list, key):
    if(list != [] and list[0] == key):
        return True
    if(list == []):
        return False
    else:
        return linearSearch(list[1:], key)


key = int(input())
list = [2, 3, 54, 1, 4, 7, 8]
if(linearSearch(list, key)):
    print("Found")
else:
    print("Not Found")

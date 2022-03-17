# finding min and max done in O(n) time
# child:2*i+1,2*i+2
# parent (i-1)//2


def maxheapify(given, n, i):
    child1 = 2*i+1
    child2 = 2*i+2
    maximum = i
    if(child1 < n and given[child1] > given[maximum]):
        maximum = child1
    if(child2 < n and given[child2] > given[maximum]):
        maximum = child2
    if(maximum != i):
        (given[maximum], given[i]) = (given[i], given[maximum])
        maxheapify(given, n, maximum)


def heapSort(given, n):
    for i in range(n-1, 0, -1):
        (given[0], given[i]) = given[i], given[0]  # swapping with last element
        maxheapify(given, i, 0)


given = [12, 11, 13, 5, 17, 7]
size = len(given)

for i in range((size//2)-1, -1, -1):
    maxheapify(given, size, i)

heapSort(given, size)
print(given)

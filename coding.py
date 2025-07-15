data = [2,1,4,5,8,6,3]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i -1):

            if array[j] >array[j+1]:
                #swap 2 elements
                array[j],array[j+1] = array[j+1], array[j]
    return array

print("array before sorting:")
print(data)
print("array after sorting:")
k = bubblesort(data)
print(k)
def bubblesort (arr):
    n = len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr [j] > arr [j+1]:
                temp = arr[j]
                arr [j] = arr [j+1]
arr = [5,1,4,2,8]
bubblesort(arr)
print("Sorted array is: ", arr)
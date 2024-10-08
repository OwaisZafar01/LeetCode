def peakIndexInMountainArray(arr):
    low = 0
    high = len(arr) -1

    while low <= high:
        mid = (low + high) //2 
        if mid > 0 and arr[mid] < arr[mid-1]:
            high = mid - 1
        elif mid < len(arr)-1 and arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            return mid
        
def findMedianSortedArrays(nums1, nums2):
    arr = nums1 + nums2
    arr.sort()
    low = 0
    high = len(arr)-1
    
    if len(arr) % 2 != 0:
        mid = (low+high)//2
        return arr[mid]
    
    else:
        a = (low + high)//2
        b = a + 1
        c = (arr[a] + arr[b]) /2
        return c


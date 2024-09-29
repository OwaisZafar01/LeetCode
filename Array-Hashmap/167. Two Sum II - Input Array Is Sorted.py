def twoSum(numbers, target):
    prevMap = {}
    for i,n in enumerate(numbers):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff]+1,i+1]
        prevMap[n] = i

    #If Not Found
    return False
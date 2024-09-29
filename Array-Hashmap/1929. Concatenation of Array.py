#Method 1
def getConcatenation(nums):
    ans = nums + nums
    return ans

#Method2
def getConcatenation(nums):
    ans = nums * 2
    return ans

#Method3
def getConcatenation(nums):
    nums.extend(nums)
    return nums

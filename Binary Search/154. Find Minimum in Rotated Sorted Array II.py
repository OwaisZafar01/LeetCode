class Solution:
    def findMin(self, nums):
        low = 0
        high = len(nums)-1

        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1

            elif nums[mid] < nums[high]:
                high = mid 

            else:
                high -=1

        return nums[low]
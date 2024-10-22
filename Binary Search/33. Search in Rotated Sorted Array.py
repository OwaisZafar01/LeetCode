class Solution:
    def search(self, nums, target):
        # Find Minimum Value
        low = 0
        n = len(nums)
        high = n-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 
                    
        min_val = low

        if min_val == 0:
            low,high = 0,n-1 

        # Target Element either right side or left side
        elif target >= nums[0] and target <= nums[min_val-1]:
            low,high = 0, min_val -1 
        else:
            low,high = min_val,n-1
        
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid -1

        return -1

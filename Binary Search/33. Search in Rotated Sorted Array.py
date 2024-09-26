def search(nums, target) :
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            
            #Left Sorted Portion
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            # Right Sorted Portion
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1
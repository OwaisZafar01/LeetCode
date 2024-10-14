class Solution:
    def searchRange(self, nums, target):

        def first_occurence(nums,target):
            low = 0
            high = len(nums)-1
            result = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    result = mid 
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return result 

        def last_occurence(nums,target):
            low = 0
            high = len(nums)-1
            result = -1
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    result = mid 
                    low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return result 

        first = first_occurence(nums,target)
        last = last_occurence(nums,target)
        
        if first != -1:
            return [first,last]

        else:
            return [-1,-1]

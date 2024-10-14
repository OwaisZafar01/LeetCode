class Solution:
    def findDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return i
            else:
                seen.add(i)
                
        return -1
        
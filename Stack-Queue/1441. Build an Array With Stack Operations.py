class Solution:
    def buildArray(self, target, n):
        stack = []
        target_set = set(target)
        for i in range(1,n+1):
            stack.append("Push")

            if i not in target_set:
                stack.append("Pop")

            if i == target[-1]:
                break
            
        return stack
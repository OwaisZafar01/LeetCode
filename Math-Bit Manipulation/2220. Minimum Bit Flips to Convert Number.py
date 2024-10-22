class Solution:
    def minBitFlips(self, start, goal):
        res = bin(start ^ goal).count("1")
        return res

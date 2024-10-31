class Solution:
    def truncateSentence(self, s, k):
        s = s.split()
        res = " ".join(s[0:k])
        return res
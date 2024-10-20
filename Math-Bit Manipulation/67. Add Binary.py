class Solution:
    def addBinary(self, a, b):
        decimal_a = int(a,2)
        decimal_b = int(b,2)
        
        decimal_sum = decimal_a + decimal_b 

        binary = bin(decimal_sum)[2:]
        return binary
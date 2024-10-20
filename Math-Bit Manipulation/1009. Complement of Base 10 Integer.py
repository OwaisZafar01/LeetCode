class Solution:
    def bitwiseComplement(self, n):
        binary = bin(n)[2:]
        complement = "".join("1" if bit == "0" else "0" for bit in binary)
        return int(complement,2)
        
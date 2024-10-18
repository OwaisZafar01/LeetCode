class Solution:
    def diagonalSum(self, mat):
        
        if not mat or not mat[0]:
            return 0

        row = len(mat)
        diagonal_sum = 0
        inverse_diagonal_sum = 0

        for i in range(row):
            diagonal_sum += mat[i][i]
            inverse_diagonal_sum += mat[i][row-1-i]

        if row % 2 == 1:
            middle_index = row // 2

            inverse_diagonal_sum -= mat[middle_index][middle_index]
            
        result = diagonal_sum + inverse_diagonal_sum
        return result
                
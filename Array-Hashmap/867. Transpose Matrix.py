class Solution:
    def transpose(self, matrix):
        if not matrix or not matrix[0]:
            return []

        new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        
        row = len(matrix)
        cols = len(matrix[0])

        for i in range(row):
            for j in range(cols):
                new_matrix[j][i] = matrix[i][j]

        return new_matrix
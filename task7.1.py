class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result.append(f"{self.matrix[i][j]:4d}")
            result.append("\n")
        return "".join(result)

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result.append(f"{self.matrix[i][j] + other.matrix[i][j]:4d}")
            result.append("\n")
        return "".join(result)


matrix1 = Matrix([[164, 25], [23, 4], [54, 126]])
matrix2 = Matrix([[74, 8], [49, 50], [113, 11]])
print(matrix1)
print(matrix1 + matrix2)
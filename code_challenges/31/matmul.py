class Matrix(object):

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def __matmul__(self, other):
        return Matrix(Matrix._multiply(self.values, other.values))

    def __rmatmul__(self, other):
        return self.__matmul__(other)

    def __imatmul__(self, other):
        self.values = self._multiply(self.values, other.values)
        return self

    @staticmethod
    def _multiply(mat1, mat2):
        return [[sum(mat1 * mat2 for mat1, mat2 in zip(mat1_row, mat2_col))
                for mat2_col in zip(*mat2)]
                for mat1_row in mat1]

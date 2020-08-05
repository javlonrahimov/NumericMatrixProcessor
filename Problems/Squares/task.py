# def sq_sum(*numbers):
#     total = 0
#     for i in numbers:
#         total += float(i) ** 2
#     return total
#
#
# def transpose_matrix(matrix):
#     result = [matrix[i] for i in reversed(range(len(matrix[0])))]
#     return result
#
#
# print(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def calculate_determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += ((-1) ** c) * matrix[0][c] * calculate_determinant(getMatrixMinor(matrix, 0, c))
    return determinant


def get_adj_matrix(matrix):
    result = [[((-1) ** (i + j)) * calculate_determinant(getMatrixMinor(matrix, i, j)) for j in matrix[i]] for i in range(len(matrix))]

    return result


print(get_adj_matrix([[2, -1, 0], [0, 1, 2], [1, 1, 0]]))


matrix = []

def index_ok(matrix, i, j) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

def calc_xmas_at(matrix, i, j) -> int:
    count = 0
    # horizontal_1
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i, j+1) and matrix[i][j+1] == 'M':
            if index_ok(matrix, i, j+2) and matrix[i][j+2] == 'A':
                if index_ok(matrix, i, j+3) and matrix[i][j+3] == 'S':
                    count += 1
    # horizontal_2
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i, j-1) and matrix[i][j-1] == 'M':
            if index_ok(matrix, i, j-2) and matrix[i][j-2] == 'A':
                if index_ok(matrix, i, j-3) and matrix[i][j-3] == 'S':
                    count += 1
    # vertical_1
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i+1, j) and matrix[i+1][j] == 'M':
            if index_ok(matrix, i+2, j) and matrix[i+2][j] == 'A':
                if index_ok(matrix, i+3, j) and matrix[i+3][j] == 'S':
                    count += 1
    # vertical_2
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i-1, j) and matrix[i-1][j] == 'M':
            if index_ok(matrix, i-2, j) and matrix[i-2][j] == 'A':
                if index_ok(matrix, i-3, j) and matrix[i-3][j] == 'S':
                    count += 1
    # diagonal_1
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i+1, j+1) and matrix[i+1][j+1] == 'M':
            if index_ok(matrix, i+2, j+2) and matrix[i+2][j+2] == 'A':
                if index_ok(matrix, i+3, j+3) and matrix[i+3][j+3] == 'S':
                    count += 1
    # diagonal_2
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i+1, j-1) and matrix[i+1][j-1] == 'M':
            if index_ok(matrix, i+2, j-2) and matrix[i+2][j-2] == 'A':
                if index_ok(matrix, i+3, j-3) and matrix[i+3][j-3] == 'S':
                    count += 1
    # diagonal_3
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i-1, j+1) and matrix[i-1][j+1] == 'M':
            if index_ok(matrix, i-2, j+2) and matrix[i-2][j+2] == 'A':
                if index_ok(matrix, i-3, j+3) and matrix[i-3][j+3] == 'S':
                    count += 1
    # diagonal_4
    if index_ok(matrix, i, j) and matrix[i][j] == 'X':
        if index_ok(matrix, i-1, j-1) and matrix[i-1][j-1] == 'M':
            if index_ok(matrix, i-2, j-2) and matrix[i-2][j-2] == 'A':
                if index_ok(matrix, i-3, j-3) and matrix[i-3][j-3] == 'S':
                    count += 1
    return count


def calc_xmas(matrix) -> int:
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            total += calc_xmas_at(matrix, i, j)
    return total


with open(input("input file name: ")) as f:
    for line in f:
        matrix.append([x for x in line.strip()])

print(calc_xmas(matrix))

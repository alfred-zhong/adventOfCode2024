
matrix = []

def index_ok(matrix, i, j) -> bool:
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])

def calc_xmas_at(matrix, i, j) -> int:
    count = 0
    if index_ok(matrix, i, j) and matrix[i][j] == 'A':
        if index_ok(matrix, i+1, j+1) and index_ok(matrix, i+1, j-1) and index_ok(matrix, i-1, j+1) and index_ok(matrix, i-1, j-1):
            if matrix[i-1][j-1] == 'M' and matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S' and matrix[i+1][j+1] == 'S':
                count += 1
            if matrix[i-1][j-1] == 'M' and matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S' and matrix[i+1][j+1] == 'S':
                count += 1
            if matrix[i-1][j+1] == 'M' and matrix[i+1][j+1] == 'M' and matrix[i+1][j-1] == 'S' and matrix[i-1][j-1] == 'S':
                count += 1
            if matrix[i+1][j+1] == 'M' and matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S' and matrix[i-1][j-1] == 'S':
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

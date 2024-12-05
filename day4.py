
# XMAS 
# SAMX
import re

def check_rows(matrix):
    cnt = 0
    for line in matrix:
        cnt += len(re.findall(r'XMAS', line)) + len(re.findall(r'SAMX', line))
    
    return cnt

def check_columns(matrix):
    rotated_matrix = []
    new_row = ""
    for i in range(len(matrix[0])):
        for row in matrix:
            new_row += row[i]
        rotated_matrix.append(new_row)
        new_row = ""
    return check_rows(rotated_matrix)

def create_diagonal_from_position(matrix, position, direction, max_pos):
    diagonal = ""
    for i in range(4):
        new_x = position[0] + i
        new_y = position[1] + (i * direction)
        if 0 <= new_x < max_pos[0] and 0 <= new_y < max_pos[1]:
            diagonal += matrix[new_x][new_y]
        else:
            return ""
    return diagonal

def create_diagonals_for_MAS(matrix, position):
    diagonal_1 = ""
    diagonal_2 = ""
    try:
        diagonal_1 += matrix[position[0] - 1][position[1] - 1]
        diagonal_1 += matrix[position[0]][position[1]]
        diagonal_1 += matrix[position[0] + 1][position[1] + 1]
        diagonal_2 += matrix[position[0] - 1][position[1] + 1]
        diagonal_2 += matrix[position[0]][position[1]]
        diagonal_2 += matrix[position[0] + 1][position[1] - 1]
    except:
        return 0

    return ("MAS" in diagonal_1 or "SAM" in diagonal_1) and ("MAS" in diagonal_2 or "SAM" in diagonal_2)

def create_diagonals(matrix):
    max_x = len(matrix)
    max_y = len(matrix[0])
    diagonals = []
    for x in range(max_x):
        for y in range(max_y):
            diagonals.append(create_diagonal_from_position(matrix, (x, y), 1, (max_x, max_y)))
            diagonals.append(create_diagonal_from_position(matrix, (x, y), -1, (max_x, max_y)))
    return diagonals

def check_diagonals(matrix):
    diagonals = create_diagonals(matrix)
    cnt = 0
    for diagonal in diagonals:
        if "XMAS" in diagonal or "SAMX" in diagonal:
            cnt += 1
    return cnt

def check_diagonal_mas(matrix):
    max_x = len(matrix)
    max_y = len(matrix[0])
    cnt = 0
    for x in range(max_x):
        for y in range(max_y):
            if matrix[x][y] == "A":
                cnt += create_diagonals_for_MAS(matrix, (x, y))
    return cnt

if __name__ == "__main__":
    total_occurences = 0
    with open("day4_input.txt", 'r') as f:
        input_matrix = f.read().split("\n")
        total_occurences += check_rows(input_matrix)
        total_occurences += check_columns(input_matrix)
        total_occurences += check_diagonals(input_matrix)
        print(check_diagonal_mas(input_matrix))
    print("|ARCHIVED|")
    print(total_occurences)
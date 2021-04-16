def spiral_matrix(size):
    number = 0
    matrix = [[0]*3 for i in range(size)]
    for row in range(size):
        for col in range(size):
            if col 
            print(row,col)
            matrix[row][col] = number + 1
            col += 1

    return matrix

if __name__ == '__main__':
    n_matrix = 3
    print(spiral_matrix(n_matrix))
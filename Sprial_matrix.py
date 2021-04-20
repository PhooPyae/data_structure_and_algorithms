def spiral_matrix(size):
    counter = 1
    matrix = [[0]*size for i in range(size)]
    start_row = 0
    end_row = size - 1
    start_column = 0
    end_column = size - 1
    while (start_row <= end_row and start_column <= end_column):
        #start row
        for i in range(start_column,end_column+1): 
            print(start_row,i)
            matrix[start_row][i] = counter
            counter += 1
        start_row += 1
        
        #right column
        for i in range(start_row,end_row+1):
            print(i,end_column)
            matrix[i][end_column] = counter 
            counter += 1
        end_column -= 1

        #end row
        for i in range(end_column,start_column-1,-1):
            print(end_row,i)
            matrix[end_row][i] = counter
            counter += 1
        end_row -= 1
        
        #left column
        for i in range(end_row,start_row-1,-1):
            print(i,start_column)
            matrix[i][start_column] = counter
            counter += 1
        start_column += 1

    return matrix

#Version 1
#Recursion
def recur_spiral(size, start_row, end_row, start_column, end_column, counter, matrix = []):
    if (counter == 1):
        print('yes')
        matrix = [[0]*size for i in range(size)]

    for i in range(start_column,end_column+1):
        matrix[start_row][i] = counter
        counter += 1
    start_row += 1

    for i in range(start_row,end_row+1):
        matrix[i][end_column] = counter
        counter += 1
    end_column -= 1

    for i in range(end_column,start_column-1,-1):
        matrix[end_row][i] = counter
        counter += 1
    end_row -= 1

    for i in range(end_row,start_row-1,-1):
        matrix[i][start_column] = counter
        counter += 1
    start_column += 1

    if (start_row <= end_row and start_column <= end_column):
        #recursion
        recur_spiral(size, start_row=start_row,end_row = end_row, start_column = start_column, end_column = end_column, counter = counter, matrix = matrix)

    return matrix

if __name__ == '__main__':
    n_matrix = 4
    print(recur_spiral(n_matrix, 0, n_matrix -1 , 0, n_matrix -1, 1, matrix = []))
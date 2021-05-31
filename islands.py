def is_visited(r,c):
    if visited_grid[r][c] == True:
        return True
    else:
        return False

def mark_as_visited(r,c):
    visited_grid[r][c] = True
    add_waiting_list(r,c)
    return True

def add_waiting_list(r,c):
    waiting_list.append([r,c])
    print('waiting list', waiting_list)
    return True

def find_next_node(r,c):
    print('Recursive: find next node of ', (r,c))
    if is_visited(r,c) == False:
        mark_as_visited(r,c)
        add_waiting_list(r,c)
        if r-1 in range(m):
            if grid[r-1][c] == '1':
                find_next_node(r-1,c)
        elif r+1 in range(m):
            if grid[r+1][col] == '1':
                find_next_node(r+1,c)
        elif c-1 in range(n):    
            if grid[r][c-1] == '1':
                find_next_node(r,c-1)
        elif c+1 in range(n):
            if grid[row-1][col] == '1':
                find_next_node(r,c+1)
    else:
        print('There is no next node')
        waiting_list.popleft([r,c])
    return True


def find_connect_edges(r,c):
    visited_count = 0
    print('find edges of ', (r,c))
    visited_count += 1
    row, col = r, c
    while len(waiting_list) >0:
        if grid[row][col] == '1':
            if is_visited(row,col) == False:
                mark_as_visited(row,col)
                add_waiting_list(row,col)
                find_next_node(row,col)
    return visited_count

def is_all_visited(v_grid):
    for i in range(len(v_grid)):
        for j in range(len(v_grid[i])):
            if j == False:
                return False
    return True

def numIslands(grid):
    num_of_island = 0
    r, c = 0, 0
    while is_all_visited(visited_grid) == False:
        num_of_island += find_connect_edges(r,c)
    return num_of_island


if __name__ == '__main__':
    # visited_grid = [[False] * n] * m
    waiting_list = []
    connected_graph = []
    grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]
    m = len(grid)
    n = len(grid[0])
    visited_grid = [[False] * n for _ in range(m)]

    print(numIslands(grid))
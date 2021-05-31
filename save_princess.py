#!/usr/bin/python
def traverse(steps, decision):
    # print('decision', decision)
    moves = ''
    for step in range(abs(steps)):
        moves = moves + "\n"+ decision
    # print('moves', moves)
    return moves

def displayPathtoPrincess(n,grid):
    princess_start = 0
    princess_end = 0
    bot_start = 0
    bot_end = 0
    move = ''
    empty_move = False
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 'p':
                princess_start = i
                princess_end = j
            elif grid[i][j] == 'm':
                bot_start = i
                bot_end = j
    
    vertical_move = princess_start - bot_start
    horizontal_move = princess_end - bot_end
    
    if vertical_move < 0:
        move = move + traverse(vertical_move, 'UP')
    elif vertical_move > 0:
        move = move + traverse(vertical_move, 'DOWN')
    if horizontal_move > 0:
        move = move + traverse(horizontal_move, 'RIGHT')
    elif horizontal_move < 0:
        move = move + traverse(horizontal_move, 'LEFT')

    return move
#print all the moves here

if __name__ == '__main__':
    m = int(input())
    grid = [] 
    for i in range(0, m): 
        grid.append(input().strip())

    print(displayPathtoPrincess(m,grid))
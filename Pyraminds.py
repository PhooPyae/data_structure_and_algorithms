import math
def pyramind(size):
    columns = size + (size-1)
    mid = math.floor(columns/2)
    stair = ''
    for row in range(size):
        for column in range(columns):
            if column == mid or mid - row <= column <= mid + row :
            # if mid - row <= column and mid + row >= column:
                stair = stair + '#'
            else:
                stair = stair + 's'
        stair = stair + '\n'
    return stair

#RECURRSIVE
# def pyramind_recur(size, row = 0, stair = ''):
#     columns = size + (size-1)
#     mid = math.floor(columns/2)

#     if row == size:
#         return
#     if len(stair)==(columns):
#         return stair
#         pyramind_recur(size,row+1)
#     if len(stair) == mid or mid - row <= len(stair) <= mid + row:
#         stair = stair + '#'
#     else:
#         stair = stair + 's'
#     stair = stair + '\n' 
#     pyramind_recur(size,row,stair)

if __name__ == '__main__':
    size = 4
    print(pyramind(size))
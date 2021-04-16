def steps(size):
    for i in range(1,size+1):
        print("#"*i+'s'*(size-i))

#version 1 with 2D arrays
def steps_v1(size):
    stair = ''
    for row in range(size):
        for column in range(size):
            if column <= row:
                stair = stair + "#"
            else:
                stair = stair + 's'
        stair = stair + '\n'
    return stair

if __name__ == '__main__':
    size = 2
    steps(size)
    print('---')
    print(steps_v1(size))

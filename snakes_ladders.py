from random import choices

def read_input():

    probability = input()
    probability = list(map(float, probability.split(',')))
    # list(map(int, T1))
    lsCount = input()
    lsCount = list(map(int, lsCount.split(',')))

    ladder = input()
    ladder = ladder.split(' ')

    ladderDict = {}
    for l in ladder:
        pair = list(map(int, l.split(',')))
        ladderDict[pair[0]] = pair[1]

    snake = input()
    snake = snake.split(' ')

    snakeDict = {}
    for l in snake:
        pair = list(map(int, l.split(',')))
        snakeDict[pair[0]] = pair[1]


    print(probability)
    print(lsCount)
    print(ladderDict)


    return (probability, lsCount, ladderDict, snakeDict)

def dice_simulation(probability):
    dice = choices(range(1, 7), probability)
    print('dice no, ',dice)
    return dice[0]

def snakes_ladders_simulation(dice_prob, ladder_snake_count, ladders_location, snakes_location):
    # ladder_count = ladder_snake_count[0]
    # snake_count = ladder_snake_count[1]
    current_loc = 0
    ladders_start_loc = ladders_location
    snakes_start_loc = snakes_location
    dice_throws = 0

    # for i in range(0,len(ladders_location),2):
    #     ladders_start_loc[ladders_location[i]] = ladders_location[i+1]

    # for i in range(0,len(snakes_location), 2):
    #     snakes_start_loc[snakes_location[i]] = snakes_location[i+1]

    while current_loc < 100:
        print('current location', current_loc)
        dice_no = dice_simulation(dice_prob)
        if current_loc in snakes_start_loc:
            current_loc = snakes_start_loc[current_loc]
            # print('go down to ', current_loc)
        elif current_loc in ladders_start_loc:
            current_loc = ladders_start_loc[current_loc]
            # print('go up to ', current_loc)
        else:
            if current_loc + dice_no == 100:
                dice_throws += 1
                return dice_throws
            elif current_loc + dice_no > 100:
                current_loc = current_loc
            else:
                current_loc = current_loc + dice_no

            # print('move forward to', current_loc)
        
        dice_throws += 1
        
            
    print('No of dice throws ', dice_throws)

    return dice_throws

if __name__ == '__main__':
    # dice_prob = [0.32,0.32,0.12,0.04,0.07,0.13]
    # ladder_snake_count = [3,7]
    # ladders_location = [32,62, 42,68, 12,98]
    # snakes_location = [95,13, 97,25, 93,37, 79,27, 75,19, 49,47, 67,17]
    # dice_prob = [0.39,0.05,0.14,0.05,0.12,0.25]
    # ladder_snake_count = [5,8]
    # ladders_location = [32,62, 44,66, 22,58, 34,60, 2,90]
    # snakes_location = [85,7 ,63,31 ,87,13 ,75,11 ,89,33 ,57,5, 71,15, 55,25]
    
    test_cases = input()
    for test in range(int(test_cases)):
        dice_prob, ls_count, ladders_loc, snakes_loc = read_input()
        simulation_times = 5000
        total_steps = 0
        average = 0
        for i in range(simulation_times):
            print('simulation times, ',i)
            total_steps += snakes_ladders_simulation(dice_prob, ls_count, ladders_loc, snakes_loc)
            print('-------------------------------------------------------------')
            print('Total steps, ',total_steps)
        average = total_steps/simulation_times
        print('Average Simulation, ',int(average))
import random
def generate():
    # number_of_pegs = random.randint(5, 20)
    number_of_pegs = 6

    pegs = []
    gears = []

    first_peg = random.randint(1, 20)
    first_gear_end = random.randint(2, 20)
    first_gear_end += 1 if first_gear_end % 2 == 1 else 0

    pegs.append(first_peg)
    gears.append(first_gear_end)

    left_end = first_peg + first_gear_end
    for _ in range(1, number_of_pegs - 1):
        right_gear_radius = random.randint(1, 20)
        gears.append(right_gear_radius)
        next_peg = left_end + right_gear_radius
        pegs.append(next_peg)
        left_end = next_peg + right_gear_radius
    
    last_gear_radius = first_gear_end // 2
    last_peg = left_end + last_gear_radius

    pegs.append(last_peg)
    gears.append(last_gear_radius)

    print(pegs)
    print(gears)
    return (pegs, gears[0])
# generate()


def solution(pegs):
    first_peg = pegs[0]
    last_peg = pegs[-1]


    for n in range(2, pegs[1]-1, 2):    
        gears = []
        radius = n
        print('radius', radius)
        first_gear_end = first_peg + radius
        last_gear_start = int(last_peg - radius/2)
        gears.append(first_gear_end)

        print('first gear', first_gear_end)
        print('last gear', last_gear_start)

        previous_radius = first_gear_end
        # previous_radius = first_gear_end
        for i in range(1, len(pegs)):
            print('i', i)
            print('len(pegs-1)', len(pegs)-1) 

            next_peg = pegs[i]    
            print('next peg', next_peg)
            
            next_gear_radius = next_peg - previous_radius
            next_gear_end = next_peg + next_gear_radius
            gears.append(next_gear_radius)
            print('Next gear radius ', next_gear_radius)
            print('Next gear end ', next_gear_end)

            previous_radius = next_gear_end
            print('previous radius', next_gear_end)
            
            if i == len(pegs)-2:
                if next_gear_end == last_gear_start:
                    gears.append(last_peg - radius/2)
                    return [n,1]
                else: break
            print('next pegs', pegs[i+1])
            if next_gear_end >= pegs[i+1]:
                print('Not ok')
                print('---------------')
                print('gears', gears)
                break
    return [-1,-1]
if __name__ == '__main__':
    peg, rad = generate()
    result = solution(peg)
    print(result)
    if result[0] == rad:
        print('Pass')    
def climbStairs(n):
    if n in cache:
       return cache[n]
    elif n < 2:
        return 1
    
    steps = climbStairs(n-1) + climbStairs(n-2)
    cache[n] = steps
    return steps

if __name__ == '__main__':
    cache = {}
    num = 5
    step = num
    print(climbStairs(num))

        
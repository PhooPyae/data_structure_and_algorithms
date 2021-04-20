def fibonacci(num):
    result = [0,1]
    for i in range(1,num):
        result.append(result[i-1]+result[i])
    print(result)
    return result[num]

#Recursion
#Version 1
def fab(num):
    if num < 2:
        return num
    return fab (num-1) + fab (num-2)

def memoi_fab(num):
    if num in cache:
        return cache[num]
    elif num < 2:
        return num

    value = fab (num-1) + fab (num-2)

    cache[num] = value
    return value


#Version 2
def recurr_fibonacci(num, result = [0,1], iterate = 1):
    if iterate < num:
        result.append(result[iterate-1]+result[iterate])
        iterate += 1
        recurr_fibonacci(num, result,iterate = iterate)
    return result[num]
    
if __name__ == '__main__':
    num = 6
    cache = {}
    value = 0
    print(fibonacci(num))
    print(recurr_fibonacci(num))
    print(fab(num))
    print(memoi_fab(num))
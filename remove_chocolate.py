cache = {}
from collections import deque
def remove_chocolate(n):
    cache = deque()
    cache.append(1)
    cache.append(1)
    cache.append(2)
    cache.append(3)
    print(cache)
    i = 3
    while i <= n:
        a = cache[1] + cache[3]
        cache.append(a)
        i += 1
        cache.popleft()
        print(cache)
    return cache[1]


def chocolate_main(n):
    result = remove_chocolate(n)
    result = (result % 1000000007)
    return result


if __name__ == '__main__':
    n = 7
    print(chocolate_main(n))